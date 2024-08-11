from logging import basicConfig, DEBUG, INFO
from helpers.settings import Settings
from time import localtime
from defaults import UTILS_DATETIME_FORMAT

def datetime_now() -> str:
    year, month, day, hour, minute, second, *_ = localtime()

    return UTILS_DATETIME_FORMAT.format(
        Y=str(year),
        M=month,
        d=day,
        h=hour,
        m=minute,
        s=second
    )

def init_logging(settings: Settings) -> None:
    basicConfig(
        level=DEBUG if settings.get_config('logging', 'level') == 'DEBUG' else INFO,
        format=settings.get_config('logging', 'format')
    )
