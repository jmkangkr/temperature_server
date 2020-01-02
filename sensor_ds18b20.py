from sensor_map import *
import os
import time
import subprocess


initialized = False


def _read_temp_raw(device_file):
    catdata = subprocess.Popen(['cat', device_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = catdata.communicate()
    out_decode = out.decode('utf-8')
    lines = out_decode.split('\n')
    return lines


def _read_temp(temp_pin):
    max_retry = 5

    fail_count = 0
    lines = _read_temp_raw(temp_pin)

    while lines[0].strip()[-3:] != 'YES' and fail_count < max_retry:
        time.sleep(0.5)
        lines = _read_temp_raw(temp_pin)
        fail_count += 1

    if fail_count < max_retry:
        equals_pos = lines[1].find('t=')

        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c
    else:
        print("Failed: {}".format(str(lines)))
        return None


def initialize(device_file_name):
    global initialized

    if not initialized:
        '''
            Have following two lines in /etc/modules file. So do not need to run modprobe. 
            w1_gpio
            w1_therm
        '''
        #os.system('modprobe w1-gpio')
        #os.system('modprobe w1-therm')
        initialized = True

    device_file_path = '/sys/bus/w1/devices/' + device_file_name + '/w1_slave'

    return device_file_path


def read_temperature(device_file_path):
    return _read_temp(device_file_path)
