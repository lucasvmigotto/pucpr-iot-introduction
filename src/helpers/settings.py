from json import loads


def get_config(data, *keys) -> str | int | None:
    if isinstance(data.get(keys[0]), dict):
        return get_config(data.get(keys[0]), *keys[1:])
    else:
        return data.get(keys[0])


class Settings:

    def __init__(self, file_path: str) -> None:
        with open(file_path, 'r') as file_ref:
            self.__config: dict = loads(file_ref.read())
            file_ref.close()

    def get_config(self, *keys) -> str | int | None:
        return get_config(self.__config, *keys)

