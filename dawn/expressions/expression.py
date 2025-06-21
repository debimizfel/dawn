from __future__ import annotations

from dataclasses import dataclass
from dawn.tokens import Token
from typing import Iterator, Protocol, override

from dawn.tokens.token import TokenKind



class Expression[T](Protocol):
    @classmethod
    def parse(cls, tokens: Iterator[Token]) -> Expression[T]: ...

    def evaluate(self) -> T: ...


#! HOMEWORK:
#! - create expressions Subtraction, Multiplication, Divistion, Negation
#! - put each expression in its own file