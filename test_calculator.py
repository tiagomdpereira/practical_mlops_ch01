import pytest

from calculator import division, product, subtract, add


def test_sum_basic() -> None:
    assert add(2.5, 3.0) == 5.5


def test_sum_edge_cases() -> None:
    assert add(0.0, 0.0) == 0.0
    assert add(-2.0, 2.0) == 0.0


def test_subtract_basic() -> None:
    assert subtract(5.3, 1.2) == pytest.approx(4.1)


def test_subtract_edge_cases() -> None:
    assert subtract(0.0, 5.0) == -5.0
    assert subtract(-3.0, -2.0) == -1.0


def test_product_basic() -> None:
    assert product(3.6, 2.0) == pytest.approx(7.2)


def test_product_edge_cases() -> None:
    assert product(0.0, 9999.0) == 0.0
    assert product(-3.0, 2.0) == -6.0


def test_division_basic() -> None:
    assert division(5.0, 2.0) == 2.5


def test_division_edge_cases() -> None:
    assert division(0.0, 2.0) == 0.0
    assert division(-9.0, 3.0) == -3.0


def test_division_by_zero_raises_assertion_error() -> None:
    with pytest.raises(AssertionError, match="b cannot be 0"):
        division(2.0, 0.0)
