"""File IO with json"""

import json

import requests


class DataPipeline:
    """Data Pipeline Routine to fetch, store and retrieve json data.

    Other information goes down here
    """

    def __init__(self, file_name):
        """Set the file name that gets used"""
        self.file_name = file_name
        
    def __str__(self) -> str:
        return "Fetch and file io of json data"

    def get_data_from_internet(self, url) -> dict:
        """Fetch data in the form of json from a given url"""
        headers = {}
        response = requests.get(url, headers=headers)
        if response.status_code in (404,):
            return {"Error": "Data Error: HTTP 404, content not found"}
        try:
            data = response.json()
        except requests.HTTPError as e:
            data = {'Error': f"HTTP Error: {e}"}
        except BaseException as e:
            data = {"Error": f"Data Error: {e}"}
        return data

    def _helper_method_that_does_nothing(self):
        return 0

    def read_file(self):
        """Read data from a file locally in json format"""
        with open(self.file_name, 'r') as fp:
            file_content = json.load(fp)
        self._helper_method_that_does_nothing()
        return file_content

    def write_file(self, data):
        """Write data to a file locally in json format"""
        with open(self.file_name, 'w') as fp:
            json.dump(data, fp)


if __name__ == '__main__':
    dp = DataPipeline('dummpy.json')
    dummy_data = dp.get_data_from_internet('http://127.0.0.1:5000/api/data')
    dp.write_file(dummy_data)
