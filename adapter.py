import json
from typing import Union, TypeVar

StringOrNone = Union[str, None]
DictOrNone = Union[dict, None]
Storage = TypeVar('Storage')

class LocalStorage:
    def __init__(self):
        self.storage = dict()

    def get(self, key: str) -> StringOrNone:
        return self.storage.get(key, None)

    def set(self, key: str, data: str) -> None:
        self.storage[key] = data

class API:
    def __init__(self, storage: TypeVar):
        self.storage = storage

    def save(self, data_dict: dict, key: str = 'new') -> None:
        self.storage.set(data_dict, key)

    def load(self, key: str = 'new') -> dict:
        return self.storage.get(key)

class Adapter:
    def __init__(self):
        self.storage = None

    def set_storage(self, storage: Storage) -> None:
        self.storage = storage

    def set(self, data_dict: dict, key: str) -> None:
        json_string = json.dumps(data_dict)
        self.storage.set(key, json_string)

    def get(self, key: str = 'new') -> DictOrNone:
        json_string = self.storage.get(key)
        return json.loads(json_string)
        

if __name__ == '__main__':
    local_storage = LocalStorage()
    storage_adapter = Adapter()
    storage_adapter.set_storage(local_storage)
    api = API(storage_adapter)

    data_to_save = {'name': 'Zsolt', 'age': 20}
    api.save(data_to_save)

    user_data: dict = api.load()
    print(user_data)
