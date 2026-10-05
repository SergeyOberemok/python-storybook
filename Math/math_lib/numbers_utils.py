from collections.abc import Generator, Iterable
import random


def getDigits(number: int | str) -> list[int]:
    letters = [*str(number).lstrip('-')]

    return [int(letter) for letter in letters]


def getTerms(number: int, maxBase: int = 10) -> list[tuple[int, int]]:
    # pairs (a, b) with a + b == number, a <= b and b a single digit of maxBase
    return [(index, number - index) for index in range(1, number) if index <= number - index < maxBase]


def generateRandomNumbers(maxNumber: int, count: int) -> Generator[int, None, None]:
    numbers = [*range(1, maxNumber)]

    for _ in range(count):
        yield random.choice(numbers)


def generateRandomNumbersPairs(maxNumber: int, count: int) -> Iterable[Iterable[int]]:
    numbersPairs = zip(generateRandomNumbers(maxNumber, count), generateRandomNumbers(maxNumber, count))

    return [*numbersPairs]
