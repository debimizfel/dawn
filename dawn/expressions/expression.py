from __future__ import annotations

from typing import Protocol


class Expression[T](Protocol):
    def evaluate(self) -> T: ...
