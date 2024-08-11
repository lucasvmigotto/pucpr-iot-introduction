import sys
from time import sleep
from machine import Pin
from components.dht11 import DHT11
from helpers.settings import Settings


SETTINGS_FILE_PATH: str = './settings.json'


def main() -> None:
    try:

        SETTINGS: Settings = Settings(SETTINGS_FILE_PATH)

        DHT11_PIN: int = SETTINGS.get_config('sensors', 'dht11')
        SLEEP_INTERVAL: int = SETTINGS.get_config('definitions', 'sleep_interval')

        sensor: DHT11 = DHT11(Pin(DHT11_PIN))

        while True:
            sensor.refresh()

            print(sensor)

            sleep(SLEEP_INTERVAL)

    except KeyboardInterrupt:
        sys.exit(0)

    except Exception as err:
        print(err)
        sys.exit(1)


if __name__ == '__main__':
    main()

