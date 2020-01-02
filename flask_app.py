from flask import Flask
import json
import datetime
import sensor
import atexit
import time
from apscheduler.schedulers.background import BackgroundScheduler
from pprint import pprint


temperature_and_humidity = None


def read_temperature_and_humidity():
    global temperature_and_humidity
    pprint("{}".format(time.strftime("%Y-%m-%d %H:%M:%S")))
    temperature_and_humidity = sensor.read_temperature_and_humidity()
    pprint(str(temperature_and_humidity))


app = Flask(__name__)


@app.route('/')
def index():
    return json.dumps(temperature_and_humidity)


if __name__ == '__main__':
    print("============ " + datetime.datetime.now().strftime('%Y-%m-d %H:%M:%S'))
    sensor.initialize()
    read_temperature_and_humidity()

    scheduler = BackgroundScheduler()
    scheduler.add_job(read_temperature_and_humidity, 'cron', minute='*')
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())

    app.run(use_reloader=False, debug=True, host='0.0.0.0')
