import unittest
from unittest import mock


from utils.xslt_utils import JingUtils, SaxonUtils


class TestSaxonUtils(unittest.TestCase):
    @mock.patch("subprocess.Popen")
    def test_saxon_process(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {"communicate.return_value": ("output".encode(), "")}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        processed_saxon = SaxonUtils(
            "path/to/saxon", "path/to/xml", "path/to/xslt"
        ).saxon_process()
        self.assertTrue(processed_saxon)

    @mock.patch("utils.xslt_utils.SaxonUtils.saxon_process")
    def test_xml_to_array(self, mock_saxon):
        mock_saxon.return_value = "some | data"
        array_from_xml = SaxonUtils(
            "path/to/saxon", "path/to/xml", "path/to/xslt"
        ).xml_to_array()
        self.assertTrue(array_from_xml)


class TestJingUtils(unittest.TestCase):
    def test_jing_process(self):

        pass

    def test_jing_process_batch(self):

        pass
