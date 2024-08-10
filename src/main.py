import sys
from handlers.wifi import WiFiHandler
from helpers.settings import init_setup

SETTINGS_FILE_PATH: str = './settings.json'

def main() -> None:
    try:

        SETTINGS: dict = init_setup(SETTINGS_FILE_PATH)

        with WiFiHandler(SETTINGS.get('SSID'), SETTINGS.get('PSWD')) as wifi:

            print(wifi.wlan.status())

    except KeyboardInterrupt:
        sys.exit(0)

    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()
