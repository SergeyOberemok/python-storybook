from math_lib.icons_utils import map_digits_to_icons, map_number_to_icons, replace_numbers_to_icons


def test_map_digits_to_icons():
    digits = [1, 2, 3]
    icons = {1: 'one', 2: 'two', 3: 'three'}
    icons_values = icons.values()

    result = map_digits_to_icons(digits, icons)

    assert all(icon in icons_values for icon in result)
    assert all(digit not in result for digit in digits)


def test_map_number_to_icons():
    number = 123
    icons = {1: 'one', 2: 'two', 3: 'three'}

    result = map_number_to_icons(number, icons)

    assert result == ''.join(icons.values())
    assert number != result


def test_replace_numbers_to_icons():
    numbers = 123, 1, 2, 3
    hello_world = f'Hello {numbers[0]} world with {numbers[1]} {numbers[2]} {numbers[3]}'
    icons = {1: 'one', 2: 'two', 3: 'three'}
    icons_values = [''.join(icons.values()), *icons.values()]

    result = replace_numbers_to_icons(hello_world, icons)

    assert all(icon in result for icon in icons_values)
    assert all(str(number) not in result for number in numbers)


def test_replace_numbers_to_icons_shorter_number_first():
    icons = {1: 'one', 2: 'two'}

    result = replace_numbers_to_icons('1 and 12', icons)

    assert result == 'one and onetwo'
