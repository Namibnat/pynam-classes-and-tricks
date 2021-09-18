"""Test Our Code

    d = DataPipeline(True)
    url = 'https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/ytd/12/1880-2016.json'
    # url = 'https://www.ncdc.noaa.gov/cag/global/time-snd_ocean/ytd/12/1880-2016.json'
    data = d.get_data_from_internet(url)
    if "Error" in data.keys():
        print(data['Error'])
    else:
        d.write_file(data)
"""

import os
import unittest

from .app import DataPipeline


class TestDataPipeline(unittest.TestCase):

    def setUp(self):
        self.test_file_name = 'test.json'
        self.data_pipeline = DataPipeline(self.test_file_name)

    def tearDown(self):
        try:
            os.remove(self.test_file_name)
        except FileNotFoundError:
            pass

    def test_get_data_from_internet_from_correct_url(self):
        url = 'https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/ytd/12/1880-2016.json'
        test_data = self.data_pipeline.get_data_from_internet(url)
        self.assertIn('description', test_data.keys())
        self.assertIn('data', test_data.keys())

    def test_get_data_from_internet_from_wrong_ulr(self):
        url = 'https://www.ncdc.noaa.gov/cag/global/time-sobe/land_ocean/ytd/12/1880-2016.json'
        test_data = self.data_pipeline.get_data_from_internet(url)
        self.assertIn('Error', test_data.keys())

    def test_get_data_from_internet_with_out_of_range_years(self):
        url = 'https://www.ncdc.noaa.gov/cag/global/time-sobe/land_ocean/ytd/12/1680-1716.json'
        test_data = self.data_pipeline.get_data_from_internet(url)
        self.assertIn('404', test_data['Error'])

    def test_write_file(self):
        url = 'https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/ytd/12/1880-2016.json'
        test_data = self.data_pipeline.get_data_from_internet(url)
        self.data_pipeline.write_file(test_data)
        with open(self.test_file_name, 'r') as fp:
            content = fp.readlines()
        str_to_test = """{"description": {"title": "Global Land"""
        self.assertIn(str_to_test, content[0])

    def test_read_file(self):
        url = 'https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/ytd/12/1880-2016.json'
        test_data = self.data_pipeline.get_data_from_internet(url)
        self.data_pipeline.write_file(test_data)
        test_file_content = self.data_pipeline.read_file()
        self.assertIn('description', test_file_content.keys())
        self.assertIn('data', test_file_content.keys())
