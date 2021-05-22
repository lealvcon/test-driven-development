import pytest
from currency.currencies.dollar import Dollar
from currency.currencies.franc import Franc

def test_dollar_multiplication():
    five = Dollar(5)
    assert Dollar(10).equals(five.times(2))
    assert Dollar(15).equals(five.times(3))


def test_dollar_equality():
    assert Dollar(5).equals(Dollar(5))

def test_franc_equality():
    assert Franc(5).equals(Franc(5))

@pytest.mark.xfail
def test_dollar_inequality():
    assert Dollar(5).equals(Dollar(6))

@pytest.mark.xfail
def test_franc_inequality():
    assert Franc(5).equals(Franc(6))

def test_franc_multiplication():
    five = Franc(5)
    assert Franc(10).equals(five.times(2))
    assert Franc(15).equals(five.times(3))