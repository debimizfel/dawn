from __future__ import annotations

from dawn.expressions.addition import Addition
from dawn.expressions.division import Division
from dawn.expressions.multiplication import Multiplication
from dawn.expressions.negation import Negation
from dawn.expressions.number_literal import NumberLiteral
from dawn.expressions.subtraction import Subtraction
from dawn.tokens import Token
from typing import Any, Iterator


from dawn.tokens import Token
from dawn.tokens.token import TokenKind
from .expression import Expression


def expression(tokens: Iterator[Token]) -> Expression[Any]:
    token = next(tokens)
    match token:
        case Token(kind=TokenKind.LITERAL, value=value):
            return NumberLiteral(float(value))
        case Token(kind=TokenKind.OPERATOR, value="add"):
            return Addition(expression(tokens), expression(tokens))
        case Token(kind=TokenKind.OPERATOR, value="sub"):
            return Subtraction(expression(tokens), expression(tokens))
        case Token(kind=TokenKind.OPERATOR, value="mul"):
            return Multiplication(expression(tokens), expression(tokens))
        case Token(kind=TokenKind.OPERATOR, value="div"):
            return Division(expression(tokens), expression(tokens))
        case Token(kind=TokenKind.OPERATOR, value="neg"):
            return Negation(expression(tokens))
        case _:
            raise ValueError(f"Unkown token {token}")
