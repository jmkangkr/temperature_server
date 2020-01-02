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
    temperature_and_humidity = {}
    for sensor_name, (sensor_type, sensor_handle) in sensor_handles.items():
        if sensor_type == SENSOR_TYPE_DS18B20:
            temperature = sensor_ds18b20.read_temperature(sensor_handle)
            humidity = None
        elif sensor_type == SENSOR_TYPE_DHT22:
            temperature, humidity = sensor_dht22.read_temperature_and_humidity(sensor_handle)
        else:
            raise RuntimeError("Invalid sensor type")
        temperature_and_humidity[sensor_name] = temperature, humidity
        time.sleep(2.0)

    return temperature_and_humidity
