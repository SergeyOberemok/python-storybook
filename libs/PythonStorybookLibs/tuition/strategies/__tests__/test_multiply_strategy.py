
from pytest import mark
from tuition.strategies.multiply_strategy import MultiplyStrategy


class TestMultiplyStrategy:
    def setup_class(self) -> None:
        self.num1 = 2
        self.num2 = 3
        self.result = self.num1 * self.num2

    def setup_method(self) -> None:
        self.strategy = MultiplyStrategy[int]((self.num1, self.num2))

    @mark.parametrize(["num1", "num2", "answer"], [(0, 0, 0), (2, 3, 6)])
    def test_doAlgorithm(self, num1: int, num2: int, answer: int) -> None:
        strategy = MultiplyStrategy[int]((num1, num2))

        result = strategy.doAlgorithm()

        assert result == answer

    @mark.parametrize(["num1", "num2", "answer"], [(2, 3, "2 * 3")])
    def test_toString(self, num1: int, num2: int, answer: str) -> None:
        strategy = MultiplyStrategy[int]((num1, num2))
        sign = "*"

        result = str(self.strategy)

        assert str(self.num1) in result
        assert str(self.num2) in result
        assert sign in result
        assert result == answer