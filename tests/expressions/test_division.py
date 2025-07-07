import pytest
from dawn.expressions.create_expression import expression
from dawn.expressions.number_literal import NumberLiteral
from dawn.expressions.division import Division
from dawn.tokens.token import Token, TokenKind


@pytest.mark.parametrize(
    "left_value, right_value, expected",
    [
        (12.0, 3.0, 4.0),
        (10.0, 4.0, 2.5),
        (-15.0, 3.0, -5.0),
        (-8.0, -2.0, 4.0),
        (7.0, 2.0, 3.5),
    ],
)
def test_evaluate_division(
    left_value: float, right_value: float, expected: float
) -> None:
    """Test division of different number combinations."""
    left = NumberLiteral(left_value)
    right = NumberLiteral(right_value)
    division = Division(left, right)
    assert division.evaluate() == expected


@pytest.mark.parametrize(
    "left_token, right_token, expected",
    [
        ("12", "3", 4.0),
        ("10", "4", 2.5),
        ("-15", "3", -5.0),
        ("-8", "-2", 4.0),
        ("7", "2", 3.5),
    ],
)
def test_parse_division(left_token: str, right_token: str, expected: float) -> None:
    """Test parsing division expressions from tokens."""
    tokens = iter(
        [
            Token(TokenKind.OPERATOR, "div"),
            Token(TokenKind.LITERAL, left_token),
            Token(TokenKind.LITERAL, right_token),
        ]
    )
    result = expression(tokens)
    assert result.evaluate() == expected
    assert isinstance(result, Division)


def test_division_by_zero() -> None:
    """Test division by zero raises ZeroDivisionError."""
    left = NumberLiteral(5.0)
    right = NumberLiteral(0.0)
    division = Division(left, right)
    with pytest.raises(ZeroDivisionError):
        division.evaluate()
