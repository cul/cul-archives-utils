import unittest
from unittest import mock

from tests.helpers import set_subprocess_mock_attrs
from cul_archives_utils.file_utils import rsync_process


class TestFileUtils(unittest.TestCase):
    @mock.patch("subprocess.Popen")
    def test_rsync_process(self, mock_subproc_popen):
        mock_subproc_popen.return_value = set_subprocess_mock_attrs()
        self.assertTrue(rsync_process("from/path", "to/path"))
