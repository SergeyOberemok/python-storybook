def getDigits(number):
    letters = [*str(number)]
    digits = list(map(lambda letter: int(letter), letters))
    return digits
