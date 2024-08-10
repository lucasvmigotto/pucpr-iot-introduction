import sys
from time import sleep
from machine import Pin
from dht import DHT11
from helpers.settings import init_setup


SETTINGS_FILE_PATH: str = './settings.json'

def main() -> None:
    try:

        SETTINGS: dict = init_setup(SETTINGS_FILE_PATH)

        sensor: DHT11 = DHT11(Pin(SETTINGS.get('SENSORS').get('dht11')))

        PRINT_TEMPLATE: str = '🌡️: {temperature:.2f}\n💧: {humidity:.2f}'

        while True:
            sensor.measure()

            print(PRINT_TEMPLATE.format(
                temperature=sensor.temperature(),
                humidity=sensor.humidity()
            ), end=f"\n{'=' * 10}\n")

            sleep(1 * .5)

    except KeyboardInterrupt:
        sys.exit(0)

    except Exception as err:
        print(err)
        sys.exit(1)


if __name__ == '__main__':
    main()
