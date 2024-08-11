import sys
from logging import Logger, getLogger
from time import sleep
from machine import Pin
from components.dht11 import DHT11
from helpers.settings import Settings
from defaults import SETTINGS_FILE_PATH
from handlers.wifi import WiFiHandler
from services.thingspeak import ThingSpeakService
from utils.main import init_logging


def main() -> None:
    try:

        SETTINGS: Settings = Settings(SETTINGS_FILE_PATH)

        init_logging(SETTINGS)
        logger: Logger = getLogger(__name__)

        DHT11_PIN: int = SETTINGS.get_config('sensors', 'dht11')
        SLEEP_INTERVAL: int = SETTINGS.get_config('definitions', 'sleep_interval')

        sensor: DHT11 = DHT11(Pin(DHT11_PIN))
        service: ThingSpeakService = ThingSpeakService(SETTINGS)

        with WiFiHandler(SETTINGS) as wifi:
            while True:
                sensor.refresh()

                service.push_to_channel(sensor)

                sleep(SLEEP_INTERVAL)

    except KeyboardInterrupt:
        logger.info('Exiting...')
        sys.exit(0)

    except Exception as err:
        logger.exception(err)
        sys.exit(1)


if __name__ == '__main__':
    main()

