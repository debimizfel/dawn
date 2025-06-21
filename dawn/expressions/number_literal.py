from __future__ import annotations

from dataclasses import dataclass
from dawn.tokens import Token
from typing import Iterator, override

from dawn.tokens.token import TokenKind

from .expression import Expression


@dataclass
class NumberLiteral(Expression[float]):
    value: float

    @classmethod
    @override
    def parse(cls, tokens: Iterator[Token]) -> NumberLiteral:
        token = next(tokens)
        assert token.kind == TokenKind.LITERAL
        value = float(token.value)
        return NumberLiteral(value)

    @override
    def evaluate(self) -> float:
        return self.value
