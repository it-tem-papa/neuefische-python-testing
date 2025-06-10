def add(a: int, b: int) -> int:
    try:
        return a + b
    except TypeError:
        raise ValueError("Both arguments must be integers.")


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    try:
        return a * b
    except TypeError:
        raise ValueError("Both arguments must be integers.")


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    try:
        return a / b
    except TypeError:
        raise ValueError("Both arguments must be integers.")
