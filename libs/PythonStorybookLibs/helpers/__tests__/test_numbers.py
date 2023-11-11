
from ..numbers import getDigits, getRandomNumbers


def test_getDigits() -> None:
    number = 123
    digits = [1, 2, 3]

    result = getDigits(number)

    assert result == digits


def test_generateRandomNumbers() -> None:
    length = 3
    minNumber = 0
    maxNumber = 10

    result = getRandomNumbers(length, minNumber, maxNumber)

    assert len(result) == length
    assert all(number >= minNumber and number <= maxNumber for number in result)