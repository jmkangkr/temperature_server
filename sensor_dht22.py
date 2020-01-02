import Adafruit_DHT


def initialize(gpio_number):
    return gpio_number


def read_temperature_and_humidity(gpio_number):
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, gpio_number)

    return temperature, humidity
