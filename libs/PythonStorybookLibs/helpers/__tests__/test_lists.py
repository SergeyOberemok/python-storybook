

from helpers.lists import getItemsRandomly


def test_getItemsRandomly() -> None:
    arr = [1, 2, 3]
    count = 5

    result = getItemsRandomly(arr, count)

    for i in result:
        assert i in arr
