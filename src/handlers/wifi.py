import network
from logging import Logger, getLogger
from time import sleep
from defaults import CONNECT_RETRY_TIMEOUT
from helpers.settings import Settings


class WiFiHandler:

    def __init__(
        self,
        settings: Settings,
        connect_retry_timeout: int = CONNECT_RETRY_TIMEOUT
    ):
        self.__logger: Logger = getLogger(__name__)
        self.__SSID: str = settings.get_config('wifi', 'ssid')
        self.__PASSWORD: str = settings.get_config('wifi', 'password')
        self.__CONNECT_RETRY_TIMEOUT: int = connect_retry_timeout
        self.wlan = None


    def __enter__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.connect(self.__SSID, self.__PASSWORD)
        while not self.wlan.isconnected():
            self.__logger.debug('Waiting for connection...')
            sleep(self.__CONNECT_RETRY_TIMEOUT)
        self.__logger.info(f'Successfully connected with IP {self.wlan.ifconfig()[0]}')
        return self


    def __exit__(self, *exception_infos):
        self.__logger.debug(f'[{self.wlan.status()}] Disconnecting...')
        self.wlan.disconnect()
        self.__logger.debug(f'[{self.wlan.status()}] Disconnected')
