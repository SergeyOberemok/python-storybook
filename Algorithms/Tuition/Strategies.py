# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Tuple

# ---

T = TypeVar('T')


# ---

# ### Generic

class Strategy(ABC, Generic[T]):
    @abstractmethod
    def doAlgorithm(self) -> T:
        pass


class CalculationStrategy(Generic[T], Strategy[T]):
    def __init__(self, numbers: Tuple[T, T] = (0, 0)):
        num1, num2 = numbers

        self.num1 = num1
        self.num2 = num2

    @abstractmethod
    def doAlgorithm(self) -> T:
        pass


# ### Addition

class AdditionStrategy(Generic[T], CalculationStrategy[T]):
    def __init__(self, numbers: Tuple[T, T] = (0, 0)):
        super().__init__(numbers)

    def doAlgorithm(self) -> T:
        return self.num1 + self.num2

    def __str__(self) -> str:
        return "%s + %s" % (self.num1, self.num2)


# #### Result

# + active=""
# print(AdditionStrategy((2, 2)).doAlgorithm())
# -

# #### ToString

# + active=""
# print(AdditionStrategy((2, 2)))
# -

# ### Multiplication

class MultiplicationStrategy(Generic[T], CalculationStrategy[T]):
    def __init__(self, numbers: Tuple[T, T] = (0, 0)):
        super().__init__(numbers)

    def doAlgorithm(self) -> T:
        return self.num1 * self.num2

    def __str__(self) -> str:
        return "%s x %s" % (self.num1, self.num2)

# #### Result

# + active=""
# print(MultiplicationStrategy((2, 3)).doAlgorithm())
# -

# #### ToString

# + active=""
# print(MultiplicationStrategy((2, 3)))
