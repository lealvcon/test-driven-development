import pytest
from currency.currencies.dollar import Dollar


def test_multiplication():
    five = Dollar(5)
    assert Dollar(10).equals(five.times(2))
    assert Dollar(15).equals(five.times(3))


def test_equality():
    assert Dollar(5).equals(Dollar(5))


@pytest.mark.xfail
def test_inequality():
    assert Dollar(5).equals(Dollar(6))
