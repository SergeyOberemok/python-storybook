
from typing import TypeVar, Generic, Tuple
from .strategy import Strategy

T = TypeVar("T")


class AddStrategy(Generic[T], Strategy[T]):
    def __init__(self, numbers: Tuple[T, T] = (0, 0)):
        num1, num2 = numbers

        self.num1 = num1
        self.num2 = num2
        self.sign = "+"

    def doAlgorithm(self) -> T:
        return self.num1 + self.num2

    def __str__(self) -> str:
        return "%s %s %s" % (self.num1, self.sign, self.num2)
