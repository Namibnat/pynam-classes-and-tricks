"""Convert between csv and json"""

import datetime
import json
import csv
import random

DATA = {}

def data_generator(n):
    now = datetime.datetime.now()
    day = 60*60*24
    for i in range(n):
        now_int = now.timestamp()
        now_int = (now_int * i) + day
        # {86400.0: {85: 0}, 1632054593.01649: {35: 1}, 3264022786.03298: {100: 2}}
        DATA[datetime.datetime.fromtimestamp(now_int).timestamp()] = {random.randint(1, 100): i}


def mk_json_data():
    data_json = json.dumps(DATA)


def make_csv_from_data():
    data = [['date', 'random_number', 'number_sq']]
    for key, value in DATA.items():
        for k, v in value.items():
            data.append([key, k, v])
    csv_str = "\n".join([','.join(str(v) for v in x) for x in data])
    with open('data.csv', 'w') as fp:
        fp.write(csv_str)
    return csv_str


if __name__ == '__main__':
    data_generator(3)
    data = make_csv_from_data()
    print(data)

