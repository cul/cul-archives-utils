from unittest import mock


def set_subprocess_mock_attrs():
    process_mock = mock.Mock()
    attrs = {"communicate.return_value": ("output".encode(), "")}
    process_mock.configure_mock(**attrs)
    return process_mock
