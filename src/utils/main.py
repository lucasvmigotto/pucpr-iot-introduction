from time import localtime


def datetime_now() -> str:
    year, month, day, hour, minute, second, *_ = localtime()

    return '{Y}-{M:02}-{d:02} {h:02}:{m:02}:{s:02}'.format(
        Y=str(year),
        M=month,
        d=day,
        h=hour,
        m=minute,
        s=second
    )
