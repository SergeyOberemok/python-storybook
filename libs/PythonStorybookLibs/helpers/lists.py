
import random

def generateListWithRandomNumbers(length: int, maxNumber: int, isZeroIncluded: bool = True) -> list:
    arr = list()

    if length <= 0:
        return arr

    for i in range(0, length):
        arr.append(random.randint(0 if isZeroIncluded else 1, maxNumber))

    return arr
