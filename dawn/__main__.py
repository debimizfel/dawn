from dawn.args import Args

from dawn.tokens.tokenizer import Tokenizer


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
        token_stream = Tokenizer(f)
        for token in token_stream:
            print(token)


if __name__ == "__main__":
    main()
