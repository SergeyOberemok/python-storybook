import numpy as np
import re
from functools import reduce

from .numbers_utils import getDigits


def mapDigitsToIcons(digits: list[int], icons: dict) -> list[str]:
    return [icons[digit] for digit in digits]


def mapNumberToIcons(number: int, icons: dict, separator: str = '') -> str:
    digits = getDigits(number)
    mappedIcons = mapDigitsToIcons(digits, icons)

    return separator.join(mappedIcons)


def replaceNumbersToIcons(message: str, icons: dict[int, str], separator: str = '') -> str:
    numbers = re.findall(r'\d+', message)
    uniqueNumbers = reduce(lambda acc, number: acc + [number] if number not in acc else acc, numbers, [])

    iconNumbers = map(lambda number: mapNumberToIcons(number, icons, separator), uniqueNumbers)
    zippedNumbersAndIcons = zip(uniqueNumbers, iconNumbers)
    result = reduce(lambda acc, numberIcon: acc.replace(str(numberIcon[0]), numberIcon[1]), zippedNumbersAndIcons, message)

    return result


def mapMatrixToIcons(M, icons):
    size = M.shape
    rowSize = size[0]
    columnSize = size[1]
    R = np.ndarray(size, dtype=object)

    for row in range(0, rowSize):
        for column in range(0, columnSize):
            if M[row, column] is None:
                R[row, column] = ""
                continue

            R[row, column] = mapNumberToIcons(M[row, column], icons)

    return R
