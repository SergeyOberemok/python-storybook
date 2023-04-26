
from helpers.lists import getRandomNumbers

def test_generateRandomNumbers() -> None:
    length = 3
    minNumber = 0
    maxNumber = 10

    result = getRandomNumbers(length, minNumber, maxNumber)

    assert len(result) == length
    assert all(number >= minNumber and number <= maxNumber for number in result)