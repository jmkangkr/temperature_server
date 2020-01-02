from flask import Flask, render_template, request, redirect, url_for
import json
import datetime
import sensor


app = Flask(__name__)


@app.route('/')
def index():
    temperature_and_humidity = sensor.read_temperature_and_humidity()
    return json.dumps(temperature_and_humidity)


if __name__ == '__main__':
    print("============ " + datetime.datetime.now().strftime('%Y-%m-d %H:%M:%S'))
    sensor.initialize()
    app.run(debug=True, host='0.0.0.0')
