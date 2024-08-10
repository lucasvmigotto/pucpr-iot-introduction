import sys
from time import sleep
from machine import Pin
from components.dht11 import DHT11
from helpers.settings import init_setup


SETTINGS_FILE_PATH: str = './settings.json'


def main() -> None:
    try:

        SETTINGS: dict = init_setup(SETTINGS_FILE_PATH)

        sensor: DHT11 = DHT11(Pin(SETTINGS.get('SENSORS').get('dht11')))

        while True:
            sensor.refresh()

            print(sensor)

            sleep(SETTINGS.get('DEFINITIONS').get('sleep_interval'))

    except KeyboardInterrupt:
        sys.exit(0)

    except Exception as err:
        print(err)
        sys.exit(1)


if __name__ == '__main__':
    main()
