from io import StringIO
import pytest
from dawn.tokens.tokenizer import Tokenizer
from dawn.tokens.token import Token, TokenKind


@pytest.mark.parametrize(
    "code,tokens",
    [
        pytest.param("", [], id="empty"),
        pytest.param("  \t\n\n ", [], id="whitespace_only"),
        pytest.param(
            "add 5 6",
            [
                Token(TokenKind.OPERATOR, "add"),
                Token(TokenKind.LITERAL, "5"),
                Token(TokenKind.LITERAL, "6"),
            ],
            id="add",
        ),
        pytest.param(
            "sub 7 8",
            [
                Token(TokenKind.OPERATOR, "sub"),
                Token(TokenKind.LITERAL, "7"),
                Token(TokenKind.LITERAL, "8"),
            ],
            id="sub",
        ),
        pytest.param(
            "mul 9 10",
            [
                Token(TokenKind.OPERATOR, "mul"),
                Token(TokenKind.LITERAL, "9"),
                Token(TokenKind.LITERAL, "10"),
            ],
            id="mul",
        ),
        pytest.param(
            "div 11 12",
            [
                Token(TokenKind.OPERATOR, "div"),
                Token(TokenKind.LITERAL, "11"),
                Token(TokenKind.LITERAL, "12"),
            ],
            id="div",
        ),
        pytest.param(
            "neg 13",
            [
                Token(TokenKind.OPERATOR, "neg"),
                Token(TokenKind.LITERAL, "13"),
            ],
            id="neg",
        ),
        pytest.param(
            "add 5 6\n",
            [
                Token(TokenKind.OPERATOR, "add"),
                Token(TokenKind.LITERAL, "5"),
                Token(TokenKind.LITERAL, "6"),
            ],
            id="trailing_newline",
        ),
        pytest.param(
            "add 5 6\nsub 7 8\n",
            [
                Token(TokenKind.OPERATOR, "add"),
                Token(TokenKind.LITERAL, "5"),
                Token(TokenKind.LITERAL, "6"),
                Token(TokenKind.OPERATOR, "sub"),
                Token(TokenKind.LITERAL, "7"),
                Token(TokenKind.LITERAL, "8"),
            ],
            id="multiple_lines",
        ),
        pytest.param(
            "  add\t5  \n 6 \t\t\n  sub 7 8  \n",
            [
                Token(TokenKind.OPERATOR, "add"),
                Token(TokenKind.LITERAL, "5"),
                Token(TokenKind.LITERAL, "6"),
                Token(TokenKind.OPERATOR, "sub"),
                Token(TokenKind.LITERAL, "7"),
                Token(TokenKind.LITERAL, "8"),
            ],
            id="mixed_whitespace",
        ),
    ],
)
def test_tokenizer(code: str, tokens: list[Token]) -> None:
    assert list(Tokenizer(StringIO(code))) == tokens
