from logging import Logger, getLogger
from urequests import Response
from urequests import request
from defaults import THINGSPEAK_BASE_URL
from enums.thingspeak import ThingSpeakApiEvent
from enums.thingspeak import ThingSpeakFieldType


class ThingSpeakAPI:

    def __init__(
        self,
        api_key_read: str,
        api_key_write: str,
        channel_code: int,
        base_url: str = THINGSPEAK_BASE_URL
    ):
        self.__logger: Logger = getLogger(__name__)
        self.__API_KEY: dict[str, str] = {
            'read': api_key_read,
            'write': api_key_write
        }
        self.__CHANNEL_CODE: int = channel_code
        self.__BASE_URL: str = base_url


    def __build_url(
        self,
        event_type: ThingSpeakApiEvent,
        endpoint: str,
        fields: dict[ThingSpeakFieldType, str | float]
    ) -> str:
        return '{base}/{endpoint}?api_key={api_key}&{query_params}'.format(
            base=self.__BASE_URL,
            endpoint=endpoint,
            api_key=self.__API_KEY.get(event_type),
            query_params='&'.join(
                f'field{str(key)}={str(value)}' for key, value in fields.items()
            )
        )


    def update_fields(self, fields: dict[int, str | float]):
        self.__logger.debug(f'Request query params: {fields}')

        response: Response = request(
            method='GET',
            url=self.__build_url(
                ThingSpeakApiEvent.WRITE,
                'update',
                fields
            )
        )

        self.__logger.debug(f'[{response.status_code}] Response: {response.content}')

        if response.status_code != 200:
            raise Exception(
                'Update was not successfully completed: {status_code} | {content}'.format(
                    status_code=response.status_code,
                    content=response.content
                )
            )

        self.__logger.info(f'Created entry #{response.text}')

        return True

