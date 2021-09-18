"""Generate a test api"""


import datetime
import random

from flask import Flask, jsonify

app = Flask(__name__)


DATA = {}


def data_generator(n):
    now = datetime.datetime.now()
    day = 60*60*24
    for i in range(n):
        now_int = now.timestamp()
        now_int = now_int + (i * day)
        # {86400.0: {85: 0}, 1632054593.01649: {35: 1}, 3264022786.03298: {100: 2}}
        DATA[datetime.datetime.fromtimestamp(now_int).timestamp()] = {random.randint(1, 100): i}


@app.route('/')
def home():
    return "<h1>Works</h1>"


@app.route('/api/data')
def api_data():
    data_generator(1000)
    return jsonify(DATA)
