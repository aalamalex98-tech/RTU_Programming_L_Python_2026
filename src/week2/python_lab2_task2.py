"""
Lab 2.2 – Comprehensions and Transformations
--------------------------------------------
Practice list, set and dictionary comprehensions.
"""

NUMBERS = [3, 8, -2, 7, 0, -5, 10]


def squares(numbers: list[int]) -> list[int]:
    """Return a list with the square of each number."""
    return [number**2 for number in numbers]


def positives(numbers: list[int]) -> list[int]:
    """Return only the numbers greater than 0."""
    return [number for number in numbers if number > 0]


def even_squares(numbers: list[int]) -> set[int]:
    """Return a set of the squares of the even numbers."""
    return {number**2 for number in numbers if number % 2 == 0}


def cubes(numbers: list[int]) -> dict[int, int]:
    """Return a dict mapping each number to its cube."""
    return {number: number**3 for number in numbers}


if __name__ == "__main__":
    print(f"Squares: {squares(NUMBERS)}")
    print(f"Positives: {positives(NUMBERS)}")
    print(f"Even squares: {even_squares(NUMBERS)}")
    print(f"Cubes: {cubes(NUMBERS)}")
