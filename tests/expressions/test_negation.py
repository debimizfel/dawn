import pytest
from dawn.expressions.create_expression import expression
from dawn.expressions.number_literal import NumberLiteral
from dawn.expressions.negation import Negation
from dawn.tokens.token import Token, TokenKind


@pytest.mark.parametrize(
    "value, expected",
    [
        (5.0, -5.0),
        (-3.0, 3.0),
        (0.0, -0.0),
        (2.5, -2.5),
        (-1.7, 1.7),
    ],
)
def test_evaluate_negation(value: float, expected: float) -> None:
    """Test negation of different numbers."""
    operand = NumberLiteral(value)
    negation = Negation(operand)
    assert negation.evaluate() == expected


@pytest.mark.parametrize(
    "token, expected",
    [
        ("5", -5.0),
        ("-3", 3.0),
        ("0", -0.0),
        ("2.5", -2.5),
        ("-1.7", 1.7),
    ],
)
def test_parse_negation(token: str, expected: float) -> None:
    """Test parsing negation expressions from tokens."""
    tokens = iter(
        [
            Token(TokenKind.OPERATOR, "neg"),
            Token(TokenKind.LITERAL, token),
        ]
    )
    result = expression(tokens)
    assert result.evaluate() == expected
    assert isinstance(result, Negation)
