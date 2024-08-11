import sys
from logging import Logger, getLogger
from time import sleep
from components.dht11 import DHT11
from components.relay import Relay
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
        RELAY_PIN: int = SETTINGS.get_config('sensors', 'relay')
        SLEEP_INTERVAL: int = SETTINGS.get_config('definitions', 'sleep_interval')
        TEMPERATURE_THRESHOLD: int = SETTINGS.get_config('definitions', 'temperature_threshold')
        HUMIDITY_THRESHOLD: int = SETTINGS.get_config('definitions', 'humidity_threshold')

        sensor: DHT11 = DHT11(DHT11_PIN)
        relay: Relay = Relay(RELAY_PIN)
        service: ThingSpeakService = ThingSpeakService(SETTINGS)

        with WiFiHandler(SETTINGS) as _wifi:
            while True:
                sensor.refresh()

                service.push_to_channel(sensor)

                relay.switch_by_dht11_state(
                    sensor,
                    TEMPERATURE_THRESHOLD,
                    HUMIDITY_THRESHOLD
                )

                sleep(SLEEP_INTERVAL)

    except KeyboardInterrupt:
        logger.info('Exiting...')
        sys.exit(0)

    except Exception as err:
        logger.exception(err)
        sys.exit(1)


if __name__ == '__main__':
    main()

