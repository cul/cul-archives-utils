import csv
import subprocess
from io import StringIO


def saxon_process(saxon_path, in_file, transform_file, out_file=None, the_params=None):
    """Process an XSLT transformation using Saxon. 

    Args:
        saxon_path (str): path to Saxon (to saxon-9.8.0.12-he.jar or similar)
        in_file (str): Path to input XML
        transform_file (str): Path to XSLT
        out_file (str): Path to output file. Use None to send to stdout. Defaults to None.
        the_params (str, optional): Additional parameters, as defined by stylesheet. Defaults to None.

    Raises:
        Exception: "SAXON ERROR: <error message>

    Returns:
        str: Result stdout
    """
    cmd = [
        "java",
        "-jar",
        saxon_path,
        in_file,
        transform_file,
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


def jing_process(jing_path, file_path, schema_path, compact=False):
    """Process an xml file against a schema (rng or schematron) using Jing. .

    Args:
        jing_path (str): Path to jing-20091111 or comparable
        file_path (str): Path to input file
        schema_path (str): Path to schema file
        compact (bool, optional): Use "compact" RelaxNG schema format. Defaults to False.

    Returns:
        str: Result stdout
    """
    # Tested with jing-20091111.
    # https://code.google.com/archive/p/jing-trang/downloads
    # -d flag (undocumented!) = include diagnostics in output.
    # -c flag is for compact schema format.
    flags = " -cd " if compact is True else " -d "
    cmd = ["java", "-jar", jing_path, flags, schema_path, file_path]
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


def xml_to_array(in_file, xslt_file, delim="|", params=" "):
    """Process XML via XSLT to tabular format, and then return as a list of lists.
    Requires XSLT that outputs delimited plain text.

    Args:
        in_file (str): path to xml file
        xslt_file (str): path to xslt file
        delim (str, optional): tabular delimiter character. Defaults to '|'.
        params (str, optional): additional XSLT parameters. Defaults to " ".

    Returns:
        list: 2-dimensional array (list of lists)
    """
    tabular = saxon_process(in_file, xslt_file, None, the_params=params)
    f = StringIO(tabular)
    return list(csv.reader(f, delimiter=delim))
