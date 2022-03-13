from typing import NamedTuple


class BaseInfo:

    def __init__(self, info: NamedTuple) -> None:
        self.info = info

    def __getattr__(self, item):
        if hasattr(self.info, item):
            return getattr(self.info, item)

        raise AttributeError(
            f"{self.__class__.__name__} object has no attribute {item}")
