
import numpy as np

from ..helpers.numbers import getDigits


def getIcons(digits: int, icons: dict) -> list:
    return [icons[digit] for digit in digits]


def mapNumberToIcons(number: int, icons: dict, separator: str = "") -> str:
    digits = getDigits(number)
    mappedIcons = getIcons(digits, icons)

    return separator.join(mappedIcons)


def mapMatrixToIcons(M, icons):
    size = M.shape
    rowSize = size[0]
    columnSize = size[1]
    R = np.ndarray(size, dtype=object)

    for row in range(0, rowSize):
        for column in range(0, columnSize):
            if M[row, column] == None:
                R[row, column] = ""
                continue

            R[row, column] = mapNumberToIcons(M[row, column], icons)

    return R


def mapDictionaryWithNumberTermsToIcons(d, icons: dict, separator=""):
    keysWithIcons = [(number, mapNumberToIcons(number, icons)) for number in d.keys()]
    R = {icon: [] for key, icon in keysWithIcons}

    for key, icon in keysWithIcons:
        numberTerms = d[key]

        for terms in numberTerms:
            term1 = mapNumberToIcons(terms[0], icons)
            term2 = mapNumberToIcons(terms[1], icons)

            termsStr = separator.join([term1, term2])
            R[icon].append(termsStr)

    return R