
import random
from faker import Faker

def getRandomNumbers(length: int, minNumber: int, maxNumber: int) -> list:
    fake = Faker()
    numbers = []

    while length > 0:
        numbers.append(fake.random.randint(minNumber, maxNumber))
        length -= 1

    return numbers