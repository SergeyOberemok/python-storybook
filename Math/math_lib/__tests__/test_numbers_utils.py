from math_lib.numbers_utils import generateRandomNumbers, generateRandomNumbersPairs, getDigits, getTerms


def test_getDigits():
    assert getDigits(123) == [1, 2, 3]
    assert getDigits(-45) == [4, 5]
    assert getDigits('67') == [6, 7]


def test_getTerms():
    assert getTerms(5) == [(1, 4), (2, 3)]
    assert getTerms(12) == [(3, 9), (4, 8), (5, 7), (6, 6)]


def test_generateRandomNumbers():
    maxNumber = 10
    count = 3

    result = [*generateRandomNumbers(maxNumber, count)]

    assert len(result) == count
    assert all(number < maxNumber for number in result)


def test_generateRandomNumbersPairs():
    maxNumber = 10
    count = 3

    result = generateRandomNumbersPairs(maxNumber, count)

    assert len(result) == count
    assert all(one < maxNumber and two < maxNumber for one, two in result)
