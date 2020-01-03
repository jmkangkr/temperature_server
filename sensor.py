from sensor_map import  *
import socket
import sensor_dht22
import sensor_ds18b20
import time


sensor_handles = {}


def initialize():
    hostname = socket.gethostname()
    for sensor in SENSOR_MAP[hostname]:
        for sensor_name, (sensor_type, sensor_unique) in sensor.items():
            if sensor_type == SENSOR_TYPE_DS18B20:
                sensor_handle = sensor_ds18b20.initialize(sensor_unique)
            elif sensor_type == SENSOR_TYPE_DHT22:
                sensor_handle = sensor_dht22.initialize(sensor_unique)
            else:
                raise RuntimeError("Invalid sensor type")
            sensor_handles[sensor_name] = (sensor_type, sensor_handle)


def read_temperature_and_humidity():
    MAX_RETRY = 3
    temperature_and_humidity = {}
    sleep_amount = 0.0
    for sensor_name, (sensor_type, sensor_handle) in sensor_handles.items():
        time.sleep(sleep_amount)
        temperature, humidity = 99.9, 99.9
        if sensor_type == SENSOR_TYPE_DS18B20:
            for _ in range(0, MAX_RETRY):
                t, h = sensor_ds18b20.read_temperature(sensor_handle), None
                if t != None:
                    temperature = t
                    humidity = h
                    break
        elif sensor_type == SENSOR_TYPE_DHT22:
            for _ in range(0, MAX_RETRY):
                t, h = sensor_dht22.read_temperature_and_humidity(sensor_handle)
                if t != None:
                    temperature = t
                    humidity = h
                    break
        else:
            raise RuntimeError("Invalid sensor type")
        temperature_and_humidity[sensor_name] = temperature, humidity
        sleep_amount = 2.0

    return temperature_and_humidity
