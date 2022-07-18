import requests


class ClioUtils(object):
    """Utilities to get data from CLIO, the Columbia Libraries Catalog"""

    def __init__(self):
        self.base_url = "https://clio.columbia.edu/catalog/"

    def get_clio_marc(self, bibid):
        """Retrieve MARC data from CLIO via http.

        Args:
            bibid (str): BIBID

        Raises:
            Exception: get_clio_marc request error

        Returns:
            binary: MARC21 data
        """
        marc_url = f"{self.base_url}{bibid}.marc"
        try:
            response = requests.get(marc_url)
            response.raise_for_status()
        except Exception as e:
            raise e
        return response.content

    def check_clio_status(self, bibid):
        """Check that a BIBID has a publicly available CLIO record.

        If using in bulk, add sleep of .5 sec or more to avoid "too many requests"
        error.

        Args:
            bibid (str): BIBID

        Returns:
            int: HTTP status code
        """
        record_url = f"{self.base_url}{bibid}"
        response = requests.get(record_url)
        return response.status_code
