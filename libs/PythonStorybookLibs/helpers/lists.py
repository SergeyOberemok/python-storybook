
import random


def getItemsRandomly(items: list, count: int) -> list:
    result = []

    for _ in range(count):
        randIndex = random.randint(0, len(items) - 1)
        item = items[randIndex]
        result.append(item)

    return result
