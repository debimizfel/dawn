from __future__ import annotations

from dataclasses import dataclass
from typing import override


from .expression import Expression


@dataclass
class NumberLiteral(Expression[float]):
    value: float

    @override
    def evaluate(self) -> float:
        return self.value
