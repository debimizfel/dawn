import pytest
from dawn.expressions.create_expression import expression
from dawn.expressions.number_literal import NumberLiteral
from dawn.tokens.token import Token, TokenKind


@pytest.mark.parametrize(
    "number, value",
    [
        ("42", 42.0),
        ("-15", -15.0),
        ("3.14", 3.14),
        ("-2.5", -2.5),
        ("0", 0.0),
    ],
)
def test_parse_number_literal(number: str, value: float) -> None:
    tokens = iter([Token(TokenKind.LITERAL, number)])
    result = expression(tokens)
    assert result.evaluate() == value
    assert isinstance(result, NumberLiteral)


@pytest.mark.parametrize("number", [42.0, -15.0, 3.14, -2.5, 0.0])
def test_evaluate_number_literal(number: float) -> None:
    """Test parsing a positive integer literal."""
    expression = NumberLiteral(number)
    assert expression.evaluate() == number
