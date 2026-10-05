import numpy as np
import re

from .numbers_utils import getDigits


def mapDigitsToIcons(digits: list[int], icons: dict) -> list[str]:
    return [icons[digit] for digit in digits]


def mapNumberToIcons(number: int | str, icons: dict, separator: str = '') -> str:
    digits = getDigits(number)
    mappedIcons = mapDigitsToIcons(digits, icons)

    return separator.join(mappedIcons)


def replaceNumbersToIcons(message: str, icons: dict[int, str], separator: str = '') -> str:
    # each whole number is replaced once, so '1' never rewrites a part of '12'
    return re.sub(r'\d+', lambda match: mapNumberToIcons(match.group(), icons, separator), message)


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
