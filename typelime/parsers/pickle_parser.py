import pickle
from collections.abc import Iterable

from typelime.parsers.base import Parser


class PickleParser[T](Parser[T]):
    def parse(self, data: bytes) -> T:
        return pickle.loads(data)

    def dump(self, data: T) -> bytes:
        return pickle.dumps(data)

    @classmethod
    def extensions(cls) -> Iterable[str]:
        return [".pkl"]