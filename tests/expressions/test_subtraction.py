import pytest
from dawn.expressions.create_expression import expression
from dawn.expressions.number_literal import NumberLiteral
from dawn.expressions.subtraction import Subtraction
from dawn.tokens.token import Token, TokenKind


@pytest.mark.parametrize(
    "left_value, right_value, expected",
    [
        (10.0, 3.0, 7.0),
        (5.0, 8.0, -3.0),
        (-4.0, -6.0, 2.0),
        (0.0, 5.0, -5.0),
        (7.5, 2.3, 5.2),
    ],
)
def test_evaluate_subtraction(
    left_value: float, right_value: float, expected: float
) -> None:
    """Test subtraction of different number combinations."""
    left = NumberLiteral(left_value)
    right = NumberLiteral(right_value)
    subtraction = Subtraction(left, right)
    if expected == 5.2:  # Handle floating point precision
        assert subtraction.evaluate() == pytest.approx(expected)
    else:
        assert subtraction.evaluate() == expected


@pytest.mark.parametrize(
    "left_token, right_token, expected",
    [
        ("10", "3", 7.0),
        ("5", "8", -3.0),
        ("-4", "-6", 2.0),
        ("0", "5", -5.0),
        ("7.5", "2.3", 5.2),
    ],
)
def test_parse_subtraction(left_token: str, right_token: str, expected: float) -> None:
    """Test parsing subtraction expressions from tokens."""
    tokens = iter(
        [
            Token(TokenKind.OPERATOR, "sub"),
            Token(TokenKind.LITERAL, left_token),
            Token(TokenKind.LITERAL, right_token),
        ]
    )
    result = expression(tokens)
    assert result.evaluate() == expected
    assert isinstance(result, Subtraction)
