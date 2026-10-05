import numpy as np
import re

from .numbers_utils import get_digits


def map_digits_to_icons(digits: list[int], icons: dict) -> list[str]:
    return [icons[digit] for digit in digits]


def map_number_to_icons(number: int | str, icons: dict, separator: str = '') -> str:
    digits = get_digits(number)
    mapped_icons = map_digits_to_icons(digits, icons)

    return separator.join(mapped_icons)


def replace_numbers_to_icons(message: str, icons: dict[int, str], separator: str = '') -> str:
    # each whole number is replaced once, so '1' never rewrites a part of '12'
    return re.sub(r'\d+', lambda match: map_number_to_icons(match.group(), icons, separator), message)


def map_matrix_to_icons(matrix, icons):
    size = matrix.shape
    row_size = size[0]
    column_size = size[1]
    result = np.ndarray(size, dtype=object)

    for row in range(0, row_size):
        for column in range(0, column_size):
            if matrix[row, column] is None:
                result[row, column] = ""
                continue

            result[row, column] = map_number_to_icons(matrix[row, column], icons)

    return result
