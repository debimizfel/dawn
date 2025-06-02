import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Self


@dataclass
class Args:
    prog: Path

    @classmethod
    def parse(cls) -> Self:
        parser = argparse.ArgumentParser(description="Dawn programming language")
        parser.add_argument("prog", type=Path, help="Path to the program to run")
        args = parser.parse_args()
        return cls(prog=args.prog)


def main() -> None:
    args = Args.parse()
    # <__main__.Args object at 0x782eb68a3230>
    #  prog = PosixPath('...')
    # ^ Args(prog=PosixPath('examples/math.dwn'))

    # print(args.prog)
    # ^ PosixPath('examples/math.dwn')

    # print(args.prog.read_text())
    # ^ 'add 5 6
    # ^  sub 7 8 ...'

    with args.prog.open() as f:
        for line in f:
            print("Line: ", line)


if __name__ == "__main__":
    main()
