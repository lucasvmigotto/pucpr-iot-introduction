from machine import Pin
from dht import DHT11 as DHT11Sensor
from utils.main import datetime_now
from defaults import (
    TEMPERATURE_ICON,
    HUMIDITY_ICON
)


class DHT11:

    def __init__(self, pin_number: int):
        self.__PIN: int = Pin(pin_number)
        self.__sensor: DHT11Sensor = DHT11Sensor(self.__PIN)
        self.__temperature: float | None = None
        self.__humidity: float | None = None
        self.__timestamp: str | None = None


    def __str__(self):
        content_template: str = '{icon} {value}'

        temperature: str = content_template.format(
            value='{:.2f}'.format(self.__temperature),
            icon=TEMPERATURE_ICON
        )

        humidity: str = content_template.format(
            value='{:.2f}'.format(self.__humidity),
            icon=HUMIDITY_ICON
        )

        output: str = ' | '.join([
            self.__timestamp,
            temperature,
            humidity
        ])

        return output


    def refresh(self):
        self.__sensor.measure()
        self.__temperature: float = self.__sensor.temperature()
        self.__humidity: float = self.__sensor.humidity()
        self.__timestamp: str = datetime_now()
        return self


    @property
    def temperature(self) -> float:
        if self.__sensor.temperature() is None:
            self.refresh()
        return self.temperature


    @property
    def humidity(self) -> float:
        if self.__humidity is None:
            self.refresh()
        return self.temperature


    @property
    def timestamp(self) -> str:
        if self.__timestamp is None:
            self.refresh()
        return self.__timestamp
