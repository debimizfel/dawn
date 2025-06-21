from __future__ import annotations

from dataclasses import dataclass
from dawn.tokens import Token
from typing import Any, Iterator, Protocol, override

from dawn.tokens.token import TokenKind


def create_expression[T = Any](tokens: Iterator[Token]) -> Expression[T]:
    raise NotImplementedError


class Expression[T](Protocol):
    @classmethod
    def parse(cls, tokens: Iterator[Token]) -> Expression[T]: ...

    def evaluate(self) -> T: ...


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


@dataclass
class AddOperation(Expression[float]):
    left: Expression[float]
    right: Expression[float]

    @classmethod
    @override
    def parse(cls, tokens: Iterator[Token]) -> AddOperation:
        token = next(tokens)
        assert token.kind == TokenKind.OPERATOR
        assert token.value == "add"

        left = create_expression(tokens)
        right = create_expression(tokens)
        return AddOperation(left, right)

    @override
    def evaluate(self) -> float:
        return self.left.evaluate() + self.right.evaluate()
