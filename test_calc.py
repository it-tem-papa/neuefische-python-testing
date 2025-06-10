import pytest
from calc import add
from calc import subtract
from calc import multiply, divide


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_positive_and_negative():
    assert add(5, -3) == 2


def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(5, 0) == 5


def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2


def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2


def test_subtract_positive_and_negative():
    assert subtract(5, -3) == 8


def test_subtract_negative_and_positive():
    assert subtract(-5, 3) == -8


def test_subtract_zero():
    assert subtract(0, 0) == 0
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5
def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6

def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6

def test_multiply_positive_and_negative():
    assert multiply(5, -3) == -15

def test_multiply_zero():
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0

def test_multiply_type_error():
    with pytest.raises(ValueError):
        multiply("a", 2)
    with pytest.raises(ValueError):
        multiply(2, "b")

def test_divide_positive_numbers():
    assert divide(6, 3) == 2.0

def test_divide_negative_numbers():
    assert divide(-6, -3) == 2.0

def test_divide_positive_and_negative():
    assert divide(6, -3) == -2.0

def test_divide_zero_numerator():
    assert divide(0, 5) == 0.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(5, 0)

def test_divide_type_error():
    with pytest.raises(ValueError):
        divide("a", 2)
    with pytest.raises(ValueError):
        divide(2, "b")



