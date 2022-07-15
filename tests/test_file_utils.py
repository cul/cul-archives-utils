import unittest
from unittest import mock

from tests.helpers import set_subprocess_mock_attrs
from utils.file_utils import file_cleanup, find_config, rsync_process


class TestFileUtils(unittest.TestCase):
    @mock.patch("subprocess.Popen")
    def test_rsync_process(self, mock_subproc_popen):
        mock_subproc_popen.return_value = set_subprocess_mock_attrs()
        self.assertTrue(rsync_process("from/path", "to/path"))

    def test_file_cleanup(self):
        """docstring for test_file_cleanup"""

    pass

    def test_find_config(self):
        """docstring for test_find_config"""

    pass
