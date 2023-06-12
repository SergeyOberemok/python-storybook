
from faker import Faker


def getDigits(number: int) -> list[int]:
    letters = [*str(number)]
    digits = [int(letter) for letter in letters]

    return digits


def getRandomNumbers(length: int, minNumber: int, maxNumber: int) -> list[int]:
    fake = Faker()
    numbers = []

    while length > 0:
        numbers.append(fake.random.randint(minNumber, maxNumber))
        length -= 1

    return numbers
