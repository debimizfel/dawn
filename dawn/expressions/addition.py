from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator, override

from .expression import Expression
from .create_expression import create_expression
from dawn.tokens import Token, TokenKind


@dataclass
class Addition(Expression[float]):
    left: Expression[float]
    right: Expression[float]

    @classmethod
    @override
    def parse(cls, tokens: Iterator[Token]) -> Addition:
        token = next(tokens)
        assert token.kind == TokenKind.OPERATOR
        assert token.value == "add"

        left = create_expression(tokens)
        right = create_expression(tokens)
        return Addition(left, right)

    @override
    def evaluate(self) -> float:
        return self.left.evaluate() + self.right.evaluate()
