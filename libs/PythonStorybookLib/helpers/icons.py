import numpy as np

from helpers.numbers import getDigits


def mapDigitsToIcons(digits: list[int], icons: dict) -> list:
    return [icons[digit] for digit in digits]


def mapNumberToIcons(number: int, icons: dict, separator: str = "") -> str:
    digits = getDigits(number)
    mappedIcons = mapDigitsToIcons(digits, icons)

    return separator.join(mappedIcons)


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
