SENSOR_TYPE_DS18B20 = 'DS18B20'
SENSOR_TYPE_DHT22 = 'DHT22'

SENSOR_MAP = {'boiler-rpi' : [{'PIPE_IN' : (SENSOR_TYPE_DS18B20, '28-020891779157')},
                              {'PIPE_OUT': (SENSOR_TYPE_DS18B20, '28-0211917790be')},
                              {'R1': (SENSOR_TYPE_DS18B20, '28-021391770d26')}, 
                              {'R2': (SENSOR_TYPE_DS18B20, '28-0214917751ce')}],
              'bedroom-rpi': [{'BED_ROOM': (SENSOR_TYPE_DHT22, '4')}],
              'kidroom-rpi': [{'KID_ROOM': (SENSOR_TYPE_DHT22, '4')}]
              }

SENSOR_NAMES = (
    'PIPE_IN',
    'PIPE_OUT',
    'R1', 
    'R2',
    'BED_ROOM',
    'KID_ROOM')
