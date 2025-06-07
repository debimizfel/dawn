
from dataclasses import dataclass
from enum import Enum


class TokenKind(Enum):
    OPERATOR = "operator"
    LITERAL = "literal"

@dataclass
class Token:
    kind: TokenKind
    value: str