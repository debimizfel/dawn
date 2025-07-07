from __future__ import annotations

from dataclasses import dataclass
from typing import override


from .expression import Expression


@dataclass
class Negation(Expression[float]):
    operand: Expression[float]

    @override
    def evaluate(self) -> float:
        return -self.operand.evaluate()
