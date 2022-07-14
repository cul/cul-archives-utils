import unittest
from unittest import mock


from utils.xml_utils import JingUtils, SaxonUtils


def set_subprocess_mock_attrs():
    process_mock = mock.Mock()
    attrs = {"communicate.return_value": ("output".encode(), "")}
    process_mock.configure_mock(**attrs)
    return process_mock


class TestSaxonUtils(unittest.TestCase):
    @mock.patch("subprocess.Popen")
    def test_saxon_process(self, mock_subproc_popen):
        mock_subproc_popen.return_value = set_subprocess_mock_attrs()
        processed_saxon = SaxonUtils(
            "path/to/saxon", "path/to/xml", "path/to/xslt"
        ).saxon_process()
        self.assertTrue(processed_saxon)

    @mock.patch("utils.xml_utils.SaxonUtils.saxon_process")
    def test_xml_to_array(self, mock_saxon):
        mock_saxon.return_value = "some | data"
        array_from_xml = SaxonUtils(
            "path/to/saxon", "path/to/xml", "path/to/xslt"
        ).xml_to_array()
        self.assertTrue(array_from_xml)


class TestJingUtils(unittest.TestCase):
    @mock.patch("subprocess.Popen")
    def test_jing_process(self, mock_subproc_popen):
        mock_subproc_popen.return_value = set_subprocess_mock_attrs()
        processed_jing = JingUtils("path/to/jing", "path/to/schema").jing_process(
            "path/to/file"
        )
        self.assertTrue(processed_jing)

    @mock.patch("subprocess.Popen")
    def test_jing_process_batch(self, mock_subproc_popen):
        mock_subproc_popen.return_value = set_subprocess_mock_attrs()
        batch_processed_jing = JingUtils(
            "path/to/jing", "path/to/schema"
        ).jing_process_batch("path/to/directory", ".xml")
        self.assertTrue(batch_processed_jing)
