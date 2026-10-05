from math_lib.numbers_utils import generate_random_numbers, generate_random_numbers_pairs, get_digits, get_terms


def test_get_digits():
    assert get_digits(123) == [1, 2, 3]
    assert get_digits(-45) == [4, 5]
    assert get_digits('67') == [6, 7]


def test_get_terms():
    assert get_terms(5) == [(1, 4), (2, 3)]
    assert get_terms(12) == [(3, 9), (4, 8), (5, 7), (6, 6)]


def test_generate_random_numbers():
    max_number = 10
    count = 3

    result = [*generate_random_numbers(max_number, count)]

    assert len(result) == count
    assert all(number < max_number for number in result)


def test_generate_random_numbers_pairs():
    max_number = 10
    count = 3

    result = generate_random_numbers_pairs(max_number, count)

    assert len(result) == count
    assert all(one < max_number and two < max_number for one, two in result)
