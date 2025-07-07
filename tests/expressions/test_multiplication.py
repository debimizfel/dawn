import pytest
from dawn.expressions.create_expression import expression
from dawn.expressions.number_literal import NumberLiteral
from dawn.expressions.multiplication import Multiplication
from dawn.tokens.token import Token, TokenKind


@pytest.mark.parametrize(
    "left_value, right_value, expected",
    [
        (4.0, 3.0, 12.0),
        (-2.0, 5.0, -10.0),
        (-3.0, -4.0, 12.0),
        (0.0, 7.0, 0.0),
        (2.5, 1.6, 4.0),
    ],
)
def test_evaluate_multiplication(
    left_value: float, right_value: float, expected: float
) -> None:
    """Test multiplication of different number combinations."""
    left = NumberLiteral(left_value)
    right = NumberLiteral(right_value)
    multiplication = Multiplication(left, right)
    assert multiplication.evaluate() == expected


@pytest.mark.parametrize(
    "left_token, right_token, expected",
    [
        ("4", "3", 12.0),
        ("-2", "5", -10.0),
        ("-3", "-4", 12.0),
        ("0", "7", 0.0),
        ("2.5", "1.6", 4.0),
    ],
)
def test_parse_multiplication(
    left_token: str, right_token: str, expected: float
) -> None:
    """Test parsing multiplication expressions from tokens."""
    tokens = iter(
        [
            Token(TokenKind.OPERATOR, "mul"),
            Token(TokenKind.LITERAL, left_token),
            Token(TokenKind.LITERAL, right_token),
        ]
    )
    result = expression(tokens)
    assert result.evaluate() == expected
    assert isinstance(result, Multiplication)
