from pytest import mark

from Strategies import MultiplicationStrategy


@mark.parametrize(["num1", "num2", "answer"], [(0, 0, 0), (2, 3, 6)])
def test_doAlgorithm(num1: int, num2: int, answer: int):
    strategy = MultiplicationStrategy[int]((num1, num2))

    result = strategy.doAlgorithm()

    assert result == answer


@mark.parametrize(["num1", "num2", "answer"], [(2, 3, "2 x 3")])
def test_toString(num1: int, num2: int, answer: str):
    strategy = MultiplicationStrategy[int]((num1, num2))

    result = str(strategy)

    assert str(num1) in result
    assert str(num2) in result
    assert result == answer
