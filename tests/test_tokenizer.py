from dataclasses import dataclass
from io import StringIO
from typing import Iterable
import pytest
from dawn.tokens.tokenizer import Tokenizer
from dawn.tokens.token import Token, TokenKind


@dataclass
class TestCase:
    code: str
    tokens: Iterable[Token]


@pytest.fixture(
    params=[
        pytest.param(TestCase("", []), id="empty"),
        pytest.param(TestCase("  \t\n\n ", []), id="whitespace_only"),
        pytest.param(
            TestCase(
                "add 5 6",
                [
                    Token(TokenKind.OPERATOR, "add"),
                    Token(TokenKind.LITERAL, "5"),
                    Token(TokenKind.LITERAL, "6"),
                ],
            ),
            id="add",
        ),
        pytest.param(
            TestCase(
                "sub 7 8",
                [
                    Token(TokenKind.OPERATOR, "sub"),
                    Token(TokenKind.LITERAL, "7"),
                    Token(TokenKind.LITERAL, "8"),
                ],
            ),
            id="sub",
        ),
        pytest.param(
            TestCase(
                "mul 9 10",
                [
                    Token(TokenKind.OPERATOR, "mul"),
                    Token(TokenKind.LITERAL, "9"),
                    Token(TokenKind.LITERAL, "10"),
                ],
            ),
            id="mul",
        ),
        pytest.param(
            TestCase(
                "div 11 12",
                [
                    Token(TokenKind.OPERATOR, "div"),
                    Token(TokenKind.LITERAL, "11"),
                    Token(TokenKind.LITERAL, "12"),
                ],
            ),
            id="div",
        ),
        pytest.param(
            TestCase(
                "neg 13",
                [
                    Token(TokenKind.OPERATOR, "neg"),
                    Token(TokenKind.LITERAL, "13"),
                ],
            ),
            id="neg",
        ),
        pytest.param(
            TestCase(
                "add 5 6\n",
                [
                    Token(TokenKind.OPERATOR, "add"),
                    Token(TokenKind.LITERAL, "5"),
                    Token(TokenKind.LITERAL, "6"),
                ],
            ),
            id="trailing_newline",
        ),
        pytest.param(
            TestCase(
                "add 5 6\nsub 7 8\n",
                [
                    Token(TokenKind.OPERATOR, "add"),
                    Token(TokenKind.LITERAL, "5"),
                    Token(TokenKind.LITERAL, "6"),
                    Token(TokenKind.OPERATOR, "sub"),
                    Token(TokenKind.LITERAL, "7"),
                    Token(TokenKind.LITERAL, "8"),
                ],
            ),
            id="multiple_lines",
        ),
        pytest.param(
            TestCase(
                "  add\t5  \n 6 \t\t\n  sub 7 8  \n",
                [
                    Token(TokenKind.OPERATOR, "add"),
                    Token(TokenKind.LITERAL, "5"),
                    Token(TokenKind.LITERAL, "6"),
                    Token(TokenKind.OPERATOR, "sub"),
                    Token(TokenKind.LITERAL, "7"),
                    Token(TokenKind.LITERAL, "8"),
                ],
            ),
            id="mixed_whitespace",
        ),
    ]
)
def case(request: pytest.FixtureRequest) -> TestCase:
    return request.param


def test_tokenizer(case: TestCase) -> None:
    code = StringIO(case.code)
    tokenizer = Tokenizer(code)
    assert list(tokenizer) == list(case.tokens)
