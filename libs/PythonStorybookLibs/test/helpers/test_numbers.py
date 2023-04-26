
from helpers.numbers import getDigits

def test_getDigits() -> None:
    number = 123
    digits = [1, 2, 3]

    result = getDigits(number)

    assert result == digits