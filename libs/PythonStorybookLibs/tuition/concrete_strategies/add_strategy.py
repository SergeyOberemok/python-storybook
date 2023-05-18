
from typing import TypeVar, Generic
from ..strategy import Strategy

T = TypeVar("T")


class AddStrategy(Generic[T], Strategy[T]):
    def __init__(self, params: tuple[T, T]) -> None:
        num1, num2 = params

        self.num1 = num1
        self.num2 = num2

    def doAlgorithm(self) -> T:
        return self.num1 + self.num2
