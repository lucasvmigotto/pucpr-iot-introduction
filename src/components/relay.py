from logging import Logger, getLogger
from machine import Pin
from components.dht11 import DHT11


class Relay(Pin):

    def __init__(
        self,
        pin_number: int
    ):
        super().__init__(pin_number, Pin.OUT)
        self.__logger: Logger = getLogger(__name__)


    def switch_by_dht11_state(
        self,
        sensor: DHT11,
        temperature_threshold: int,
        humidity_threshold: int
    ) -> None:
        if (
            sensor.temperature > temperature_threshold
            or sensor.humidity > humidity_threshold
        ):
            self.__logger.debug('Set relay to ON')
            self.on()
        else:
            self.__logger.debug('Set relay to OFF')
            self.off()
