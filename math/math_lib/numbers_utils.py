from collections.abc import Generator, Iterable
import random


def get_digits(number: int | str) -> list[int]:
    letters = [*str(number).lstrip('-')]

    return [int(letter) for letter in letters]


def get_terms(number: int, max_base: int = 10) -> list[tuple[int, int]]:
    # pairs (a, b) with a + b == number, a <= b and b a single digit of max_base
    return [(index, number - index) for index in range(1, number) if index <= number - index < max_base]


def generate_random_numbers(max_number: int, count: int) -> Generator[int, None, None]:
    numbers = [*range(1, max_number)]

    for _ in range(count):
        yield random.choice(numbers)


def generate_random_numbers_pairs(max_number: int, count: int) -> Iterable[Iterable[int]]:
    numbers_pairs = zip(generate_random_numbers(max_number, count), generate_random_numbers(max_number, count))

    return [*numbers_pairs]
