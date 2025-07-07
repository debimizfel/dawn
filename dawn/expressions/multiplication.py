from __future__ import annotations

from dataclasses import dataclass
from typing import override


from .expression import Expression


@dataclass
class Multiplication(Expression[float]):
    left: Expression[float]
    right: Expression[float]

    @override
    def evaluate(self) -> float:
        return self.left.evaluate() * self.right.evaluate()
