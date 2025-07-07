from dawn.expressions.number_literal import NumberLiteral
from dawn.expressions.addition import Addition
from dawn.expressions.subtraction import Subtraction
from dawn.expressions.multiplication import Multiplication
from dawn.expressions.division import Division
from dawn.expressions.negation import Negation


def test_nested_addition() -> None:
    """Test addition with nested expressions."""
    # (5 + 3) + (2 + 1) = 11
    left_inner = Addition(NumberLiteral(5.0), NumberLiteral(3.0))
    right_inner = Addition(NumberLiteral(2.0), NumberLiteral(1.0))
    outer = Addition(left_inner, right_inner)
    assert outer.evaluate() == 11.0


def test_mixed_operations() -> None:
    """Test mixing different operations."""
    # (10 - 5) * 2 = 10
    subtraction = Subtraction(NumberLiteral(10.0), NumberLiteral(5.0))
    multiplication = Multiplication(subtraction, NumberLiteral(2.0))
    assert multiplication.evaluate() == 10.0


def test_negation_with_addition() -> None:
    """Test negation of an addition expression."""
    # -(5 + 3) = -8
    addition = Addition(NumberLiteral(5.0), NumberLiteral(3.0))
    negation = Negation(addition)
    assert negation.evaluate() == -8.0


def test_division_with_multiplication() -> None:
    """Test division of multiplication result."""
    # (4 * 3) / 2 = 6
    multiplication = Multiplication(NumberLiteral(4.0), NumberLiteral(3.0))
    division = Division(multiplication, NumberLiteral(2.0))
    assert division.evaluate() == 6.0


def test_complex_nested_expression() -> None:
    """Test a complex nested expression."""
    # ((10 + 5) * 2) - (8 / 4) = 28
    addition = Addition(NumberLiteral(10.0), NumberLiteral(5.0))
    multiplication = Multiplication(addition, NumberLiteral(2.0))
    division = Division(NumberLiteral(8.0), NumberLiteral(4.0))
    final_subtraction = Subtraction(multiplication, division)
    assert final_subtraction.evaluate() == 28.0
