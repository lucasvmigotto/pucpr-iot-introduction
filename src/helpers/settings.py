from json import loads


def init_setup(file_path: str) -> dict[str, str]:
    with open(file_path) as file_ref:
        SETTINGS: dict = loads(file_ref.read())
        file_ref.close()

    return {
        'DEFINITIONS': SETTINGS.get('definitions'),

        'SENSORS': SETTINGS.get('sensors'),

        'SSID': SETTINGS.get('wifi').get('ssid'),
        'PSWD': SETTINGS.get('wifi').get('password'),

        'THINGSPEAK_CHANNEL_CODE': SETTINGS\
            .get('thingspeak')\
            .get('channel'),

        'THINGSPEAK_API_KEY_READ': SETTINGS\
            .get('thingspeak')\
            .get('apikey')\
            .get('read'),

        'THINGSPEAK_API_KEY_WRITE': SETTINGS\
            .get('thingspeak')\
            .get('apikey')\
            .get('read')
    }
