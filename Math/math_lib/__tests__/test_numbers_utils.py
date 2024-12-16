from numbers_utils import generateRandomNumbers, generateRandomNumbersPairs


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
