import pytest
from calc import add
from calc import subtract


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
    
def test_add_raises_value_error_on_invalid_types():
    with pytest.raises(ValueError, match="Both arguments must be integers."):
        add(2, "e")
    with pytest.raises(ValueError, match="Both arguments must be integers."):
        add("a", 3)
    with pytest.raises(ValueError, match="Both arguments must be integers."):
        add("a", "b")
    with pytest.raises(ValueError, match="Both arguments must be integers."):
        add(2.5, 3)
    with pytest.raises(ValueError, match="Both arguments must be integers."):
        add(2, None)

