import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Self


@dataclass  # create a dataclass for Args
class Args:
    prog: Path

    @classmethod
    def parse(cls) -> Self:
        parser = argparse.ArgumentParser(description="Dawn programming language")
        parser.add_argument("prog", type=Path, help="Path to the program to run")
        args = parser.parse_args()
        return cls(prog=args.prog)
