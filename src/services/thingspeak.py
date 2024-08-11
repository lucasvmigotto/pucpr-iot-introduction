from logging import Logger, getLogger
from components.dht11 import DHT11
from enums.thingspeak import ThingSpeakFieldType
from helpers.thingspeak import ThingSpeakAPI
from helpers.settings import Settings


class ThingSpeakService:

    def __init__(self, settings: Settings):
        self.__logger: Logger = getLogger(__name__)
        self.__SETTINGS = settings
        self.__API: ThingSpeakAPI = ThingSpeakAPI(
            api_key_read=self.__SETTINGS \
                .get_config('thingspeak', 'apikey', 'read'),
            api_key_write=self.__SETTINGS \
                .get_config('thingspeak', 'apikey', 'write'),
            channel_code=self.__SETTINGS \
                .get_config('thingspeak', 'channel')
        )

    def push_to_channel(self, sensor: DHT11) -> bool:
        try:
            self.__API.update_fields({
                ThingSpeakFieldType.TIMESTAMP: sensor.timestamp,
                ThingSpeakFieldType.TEMPERATURE: sensor.temperature,
                ThingSpeakFieldType.HUMIDITY: sensor.humidity
            })

            return True

        except Exception as err:
            self.__logger.exception(
                'Failed to push stats to ThingSpeak channel {channel_code}: {err}'.format(
                    channel_code=self.__SETTINGS.get_config(
                        'thingspeak', 'channel'
                    ),
                    err=err.args
                )
            )
            return False
