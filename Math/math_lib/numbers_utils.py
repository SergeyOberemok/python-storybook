from collections.abc import Generator, Iterable
import random


def getDigits(number: int) -> list[int]:
    letters = [*str(number)]

    return [int(letter) for letter in letters]


def getTerms(number, maxBase=10):
    terms = []

    for index, term in enumerate(range(number, 0, -1)):
        if index == 0:
            continue

        if number == index + term and index <= term < maxBase:
            terms.append((index, term))

    return terms


def generateRandomNumbers(maxNumber: int, count: int) -> Generator[int, None, None]:
    numbers = [*range(1, maxNumber)]

    for _ in range(count):
        yield random.choice(numbers)


def generateRandomNumbersPairs(maxNumber: int, count: int) -> Iterable[Iterable[int]]:
    numbersPairs = zip(generateRandomNumbers(maxNumber, count), generateRandomNumbers(maxNumber, count))

    return [*numbersPairs]
