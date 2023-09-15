from typing import Dict, Any


class SingletonMeta(type):
    _intances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._intances:
            cls._intances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._intances[cls]


class Bag(object, metaclass=SingletonMeta):
    pass
