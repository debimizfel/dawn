from __future__ import annotations

from dawn.tokens import Token
from typing import Any, Iterator

from dawn.tokens import Token
from .expression import Expression


def create_expression[T = Any](tokens: Iterator[Token]) -> Expression[T]:
    raise NotImplementedError
