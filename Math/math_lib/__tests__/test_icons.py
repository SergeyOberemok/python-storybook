from icons_utils import mapDigitsToIcons, mapNumberToIcons, replaceNumbersToIcons


def test_mapDigitsToIcons():
    digits = [1, 2, 3]
    icons = {1: 'one', 2: 'two', 3: 'three'}
    iconsValues = icons.values()

    result = mapDigitsToIcons(digits, icons)

    assert all(icon in iconsValues for icon in result)
    assert all(digit not in result for digit in digits)


def test_mapNumberToIcons():
    number = 123
    icons = {1: 'one', 2: 'two', 3: 'three'}

    result = mapNumberToIcons(number, icons)

    assert result == ''.join(icons.values())
    assert number != result


def test_replaceNumbersToIcons():
    numbers = 123, 1, 2, 3
    helloWorld = f'Hello {numbers[0]} world with {numbers[1]} {numbers[2]} {numbers[3]}'
    icons = {1: 'one', 2: 'two', 3: 'three'}
    iconsValues = [''.join(icons.values()), *icons.values()]

    result = replaceNumbersToIcons(helloWorld, icons)

    assert all(icon in result for icon in iconsValues)
    assert all(str(number) not in result for number in numbers)
