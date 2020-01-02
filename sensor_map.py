SENSOR_TYPE_DS18B20 = 'DS18B20'
SENSOR_TYPE_DHT22 = 'DHT22'

SENSOR_MAP = {'boiler-rpi'  : [{'IN_PIPE_SENSOR'          : (SENSOR_TYPE_DS18B20, '28-031097797ecf')},
                               {'OUT_LIVING_ROOM0_SENSOR' : (SENSOR_TYPE_DS18B20, '28-0307977984ce')},
                               {'OUT_LIVING_ROOM1_SENSOR' : (SENSOR_TYPE_DS18B20, '28-0307977989bd')},
                               {'OUT_BED_ROOM_SENSOR'     : (SENSOR_TYPE_DS18B20, '28-0309977917ea')},
                               {'OUT_COMPUTER_ROOM_SENSOR': (SENSOR_TYPE_DS18B20, '28-031197798c66')},
                               {'OUT_HANS_ROOM_SENSOR'    : (SENSOR_TYPE_DS18B20, '28-030897790650')}],
              'bedroom-rpi' : [{'BED_ROOM_SENSOR':  (SENSOR_TYPE_DHT22, '4')}],
              'hansroom-rpi': [{'HANS_ROOM_SENSOR': (SENSOR_TYPE_DHT22, '4')}]
              }

SENSOR_NAMES = (
    'IN_PIPE_SENSOR',
    'OUT_LIVING_ROOM0_SENSOR',
    'OUT_LIVING_ROOM1_SENSOR',
    'OUT_BED_ROOM_SENSOR',
    'OUT_COMPUTER_ROOM_SENSOR',
    'OUT_HANS_ROOM_SENSOR',
    'BED_ROOM_SENSOR',
    'HANS_ROOM_SENSOR')
