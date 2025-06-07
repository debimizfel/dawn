from typing import Generator, TextIO
from dawn.tokens.token import Token, TokenKind


class Tokenizer:
    _OPERATORS = {"add", "sub", "mul", "div", "neg"}

    def __init__(self, code: TextIO) -> None:
        self._code = code

    # converitr self.code a tokens
    # yield devuelve un resultado a la vez.
    def __iter__(self) -> Generator[Token]:
        for line in self._code:
            yield from self._tokenize_line(line)

    # input: "add 5 6"
    # output: Token(TokenKinds.OPERATOR, "add")
    # output: Token(TK.LITERAL, "5")
    # output: Token(TK.LITERAL, "6")
    def _tokenize_line(self, line: str) -> Generator[Token]:
        for word in line.split():
            yield self._tokenize_word(word)

    def _tokenize_word(self, word: str) -> Token:
        if word in self._OPERATORS:
            return Token(TokenKind.OPERATOR, word)
        return Token(TokenKind.LITERAL, word)
