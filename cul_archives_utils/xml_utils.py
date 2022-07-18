import csv
import subprocess
from io import StringIO


class SaxonUtils(object):
    """Utilities using the Saxon XSLT processor."""

    def __init__(self, saxon_path, xml_file, xslt_file):
        """Sets filepaths to Saxon executable, XML file to transform, and XSLT file.

        Args:
            saxon_path (str): path to Saxon (to saxon-9.8.0.12-he.jar or similar)
            xml_file (str): Path to input XML
            xslt_file (str): Path to XSLT
        """
        self.saxon_path = saxon_path
        self.xml_file = xml_file
        self.xslt_file = xslt_file

    def saxon_process(self, out_file=None, the_params=None):
        """Process an XSLT transformation using Saxon.

        Args:
            out_file (str): Path to output file. Use None to send to stdout.
            the_params (str, optional): Additional parameters, as defined by stylesheet.

        Raises:
            Exception: "SAXON ERROR: <error message>

        Returns:
            str: Result stdout
        """
        cmd = [
            "java",
            "-jar",
            self.saxon_path,
            self.xml_file,
            self.xslt_file,
            "--suppressXsltNamespaceCheck:on",
        ]
        if out_file:
            cmd.append(f" > {out_file}")
        if the_params:
            cmd.insert(5, the_params)
        p = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
        result = p.communicate()
        if not result[1]:
            return result[0].decode("utf-8")
        else:
            raise Exception(result[1].decode("utf-8"))

    def xml_to_array(self, delim="|", params=" "):
        """Process XML via XSLT to tabular format, and then return as a list of lists.

        Requires XSLT that outputs delimited plain text.

        Args:
            delim (str, optional): tabular delimiter character. Defaults to '|'.
            params (str, optional): additional XSLT parameters. Defaults to " ".

        Returns:
            list: 2-dimensional array (list of lists)
        """
        tabular = self.saxon_process(the_params=params)
        f = StringIO(tabular)
        return list(csv.reader(f, delimiter=delim))


class JingUtils(object):
    """Utilities using Jing."""

    def __init__(self, jing_path, schema_path, compact=False):
        """Sets filepaths to jing executable and schema, and whether to use "compact" RelaxNG schema format.

        Args:
            jing_path (str): Path to jing-20091111 or comparable
            schema_path (str): Path to schema file
            compact (bool, optional): Use "compact" RelaxNG schema format
        """
        self.jing_path = jing_path
        self.schema_path = schema_path
        self.flags = "-cd" if compact is True else "-d"

    def jing_process(self, file_path):
        """Process an xml file against a schema (rng or schematron) using Jing.

        Args:
            file_path (str): Path to input file

        Returns:
            str: Result stdout
        """
        # Tested with jing-20091111.
        # https://code.google.com/archive/p/jing-trang/downloads
        # -d flag (undocumented!) = include diagnostics in output.
        # -c flag is for compact schema format.
        cmd = ["java", "-jar", self.jing_path, self.flags, self.schema_path, file_path]
        p = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
        result = p.communicate()
        if result[1]:
            raise Exception(result[1].decode("utf-8"))
        else:
            return result[0].decode("utf-8")

    def jing_process_batch(self, data_folder, pattern):
        """Process a set of xml files within a directory against a schema (rng or schematron) using Jing.

        Xargs batches files so they won't exceed limit on arguments with thousands of files.

        Args:
            data_folder (str): path to directory to process
            pattern (str): matching expression for files (see 'find' command)

        Returns:
            str: Result stdout
        """
        cmd = [
            "find",
            data_folder,
            "-name",
            f'"{pattern}"',
            "|",
            "xargs",
            "-L",
            "128",
            "java",
            "-jar",
            self.jing_path,
            self.flags,
            self.schema_path,
        ]
        p = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
        result = p.communicate()
        if result[1]:
            raise Exception(result[1].decode("utf-8"))
        else:
            return result[0].decode("utf-8")
