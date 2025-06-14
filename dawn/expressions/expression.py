from dawn.tokens import Token
from typing import Iterator, Protocol, Self


class Expression[T](Protocol):
    @classmethod
    def parse(cls, tokens: Iterator[Token]) -> Self: ...

    def evaluate(self) -> T: ...
