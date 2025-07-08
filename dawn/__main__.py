from dawn.args import Args

from dawn.expressions.create_expression import expression
from dawn.tokens import Tokenizer


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
        tokens = Tokenizer(f)
        while True:
            try:
                expr = expression(iter(tokens))
                print(expr.evaluate())
            except StopIteration:
                break


if __name__ == "__main__":
    main()
