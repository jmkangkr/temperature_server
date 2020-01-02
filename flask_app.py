from flask import Flask
import json
import datetime
import sensor
import atexit
import time
from apscheduler.scheduler import Scheduler


def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


scheduler = Scheduler()
scheduler.add_interval_job(print_date_time, seconds=60, start_date='2020-01-01 00:00')
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


app = Flask(__name__)


@app.route('/')
def index():
    temperature_and_humidity = sensor.read_temperature_and_humidity()
    return json.dumps(temperature_and_humidity)


if __name__ == '__main__':
    print("============ " + datetime.datetime.now().strftime('%Y-%m-d %H:%M:%S'))
    sensor.initialize()
    app.run(debug=True, host='0.0.0.0')
