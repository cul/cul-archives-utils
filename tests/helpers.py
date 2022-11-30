from pathlib import Path
from unittest import mock

from googleapiclient.discovery import build
from googleapiclient.http import HttpMock

FIXTURES_PATH = "fixtures"


def set_subprocess_mock_attrs():
    process_mock = mock.Mock()
    attrs = {"communicate.return_value": ("output".encode(), "")}
    process_mock.configure_mock(**attrs)
    return process_mock


def mock_build_service():
    http = HttpMock(Path(FIXTURES_PATH, "discovery.json"), {"status": "200"})
    service = build("sheets", "v4", http=http)
    return service


def mock_get_sheet_info(fixture_name):
    service = mock_build_service()
    request = service.spreadsheets().get(
        spreadsheetId="spreadsheet_it", includeGridData=False
    )
    http = HttpMock(Path(FIXTURES_PATH, fixture_name))
    response = request.execute(http=http)
    return response
