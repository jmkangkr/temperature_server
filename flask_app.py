from flask import Flask
import json
import datetime
import sensor
import atexit
import time
from apscheduler.schedulers.background import BackgroundScheduler
import logging
from logging.handlers import TimedRotatingFileHandler
import os


log = None


temperature_and_humidity = None


def read_temperature_and_humidity():
    global temperature_and_humidity
    log.info("Update temperature and humidity")
    temperature_and_humidity = sensor.read_temperature_and_humidity()
    log.info("{}".format(temperature_and_humidity))

    error_sensors = []
    for sens, value in temperature_and_humidity.items():
        if value[0] == None:
            log.warning("Couldn't read temperature")
            error_sensors.append(sens)

    for sens in error_sensors:
        temperature_and_humidity[sens] = (99.9, 99.9)

    log.info(str(temperature_and_humidity))


app = Flask(__name__)


@app.route('/')
def index():
    return json.dumps(temperature_and_humidity)


def setup_logger(logger_name, log_dir_name, log_file_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    try:
        os.makedirs(log_dir_name)
    except FileExistsError:
        pass

    fh = TimedRotatingFileHandler(os.path.join(log_dir_name, log_file_name), when="midnight", backupCount=14)

    fh.setLevel(logging.NOTSET)

    ch = logging.StreamHandler()
    ch.setLevel(logging.NOTSET)

    #formatter = logging.Formatter('%(message)s')
    #ch.setFormatter(formatter)
    #fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


if __name__ == '__main__':
    log = setup_logger(__name__, 'logs', 'temp_server.log')

    sensor.initialize()
    read_temperature_and_humidity()

    scheduler = BackgroundScheduler()
    scheduler.add_job(read_temperature_and_humidity, 'cron', minute='*')
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())

    app.run(use_reloader=False, debug=True, host='0.0.0.0')
