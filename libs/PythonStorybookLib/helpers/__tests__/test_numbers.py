from helpers.numbers import getDigits, getTerms


def test_getDigits():
    number = 123

    result = getDigits(number)

    for letter in str(number):
        assert int(letter) in result


def test_getTerms():
    number = 4

    result = getTerms(number)

    assert len(result) > 0

    for num1, num2 in result:
        assert num1 + num2 == number
