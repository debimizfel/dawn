import pytest
from dawn.expressions.create_expression import expression
from dawn.expressions.number_literal import NumberLiteral
from dawn.expressions.addition import Addition
from dawn.tokens.token import Token, TokenKind


@pytest.mark.parametrize(
    "left_value, right_value, expected",
    [
        (5.0, 3.0, 8.0),
        (-4.0, -6.0, -10.0),
        (10.0, -3.0, 7.0),
        (5.0, 0.0, 5.0),
        (2.5, 3.7, 6.2),
    ],
)
def test_evaluate_addition(
    left_value: float, right_value: float, expected: float
) -> None:
    """Test addition of different number combinations."""
    left = NumberLiteral(left_value)
    right = NumberLiteral(right_value)
    addition = Addition(left, right)
    assert addition.evaluate() == expected


@pytest.mark.parametrize(
    "left_token, right_token, expected",
    [
        ("5", "3", 8.0),
        ("-4", "-6", -10.0),
        ("10", "-3", 7.0),
        ("5", "0", 5.0),
        ("2.5", "3.7", 6.2),
    ],
)
def test_parse_addition(left_token: str, right_token: str, expected: float) -> None:
    """Test parsing addition expressions from tokens."""
    tokens = iter(
        [
            Token(TokenKind.OPERATOR, "add"),
            Token(TokenKind.LITERAL, left_token),
            Token(TokenKind.LITERAL, right_token),
        ]
    )
    result = expression(tokens)
    assert result.evaluate() == expected
    assert isinstance(result, Addition)
