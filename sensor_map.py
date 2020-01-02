SENSOR_TYPE_DS18B20 = 'DS18B20'
SENSOR_TYPE_DHT22 = 'DHT22'

SENSOR_MAP = {'boiler-rpi' : [{'OUT_LIVING_ROOM0' : (SENSOR_TYPE_DS18B20, '28-0307977984ce')},
                              {'OUT_KID_ROOM'     : (SENSOR_TYPE_DS18B20, '28-030897790650')},
                              {'OUT_BED_ROOM'     : (SENSOR_TYPE_DS18B20, '28-0309977917ea')},
                              {'OUT_LIVING_ROOM1' : (SENSOR_TYPE_DS18B20, '28-0307977989bd')},
                              {'OUT_COMPUTER_ROOM': (SENSOR_TYPE_DS18B20, '28-031197798c66')},
                              {'PIPE_IN'          : (SENSOR_TYPE_DS18B20, '28-031097797ecf')}],
              'bedroom-rpi': [{'BED_ROOM': (SENSOR_TYPE_DHT22, '4')}],
              'kidroom-rpi': [{'KID_ROOM': (SENSOR_TYPE_DHT22, '4')}]
              }

SENSOR_NAMES = (
    'OUT_LIVING_ROOM0',
    'OUT_KID_ROOM',
    'OUT_BED_ROOM',
    'OUT_LIVING_ROOM1',
    'OUT_COMPUTER_ROOM',
    'PIPE_IN',
    'BED_ROOM',
    'KID_ROOM')
