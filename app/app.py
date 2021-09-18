"""File IO with json

load
loads
dump
dumps
"""

import json

import requests


class DataPipeline:

    def __init__(self, some_class_var):
        self.some_class_var = some_class_var

    def __str__(self) -> str:
        return "Fetch and file io of json data"

    def get_data_from_internet(self, url) -> dict:
        try:
            content = requests.get(url)
            data = content.json()
        except BaseException as e:
            data = {"Error": f"Data Error: {e}"}
        return data

    def read_file(self):
        with open('file.json', 'r') as fp:
            file_content = json.load(fp)
        return file_content

    def write_file(self, data):
        with open('file.json', 'w') as fp:
            json.dump(data, fp)
            


def main():
    d = DataPipeline(True)
    url = 'https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/ytd/12/1880-2016.json'
    # url = 'https://www.ncdc.noaa.gov/cag/global/time-snd_ocean/ytd/12/1880-2016.json'
    data = d.get_data_from_internet(url)
    if "Error" in data.keys():
        print(data['Error'])
    else:
        d.write_file(data)


if __name__ == '__main__':
    main()