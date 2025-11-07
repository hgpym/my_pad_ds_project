from typing import List


def hello_world() -> str:
    """Return hello world message."""
    print("Hello from resolved conflict!")
    return "Hello World - RESOLVED"


def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def new_function() -> str:
    """A new function."""
    return "This is new"


def another_function() -> str:
    """Another function."""
    return "This is another function"


def calculate_sum(numbers: List[int]) -> int:
    """Calculate sum of numbers."""
    return sum(numbers)
