def getDigits(number: int) -> list[int]:
    letters = [*str(number)]

    return [int(letter) for letter in letters]


def getTerms(number, maxBase=10):
    terms = []

    for index, term in enumerate(range(number, 0, -1)):
        if index == 0:
            continue

        if number == index + term and index <= term < maxBase:
            terms.append((index, term))

    return terms
