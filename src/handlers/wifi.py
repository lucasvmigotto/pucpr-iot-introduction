import network
from time import sleep
from defaults import CONNECT_RETRY_TIMEOUT


class WiFiHandler:

    def __init__(
        self, ssid:
        str, password: str,
        connect_retry_timeout: int = CONNECT_RETRY_TIMEOUT
    ):
        self.__SSID: str = ssid
        self.__PASSWORD: str = password
        self.__CONNECT_RETRY_TIMEOUT: int = connect_retry_timeout
        self.wlan = None


    def __enter__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.connect(self.__SSID, self.__PASSWORD)
        while not self.wlan.isconnected():
            print('Waiting for connection...')
            sleep(self.__CONNECT_RETRY_TIMEOUT)
        print(f'Successfully connected with IP {self.wlan.ifconfig()[0]}')
        return self


    def __exit__(self, *exception_infos):
        print(f'[{self.wlan.status()}] Disconnecting...')
        self.wlan.disconnect()
        print(f'[{self.wlan.status()}] Disconnected')
