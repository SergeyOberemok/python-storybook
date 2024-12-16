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
#     display_name: Python [conda env:base] *
#     language: python
#     name: conda-base-py
# ---

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from collections.abc import Iterable
from functools import reduce

from Strategy import Strategy

# ---

T = TypeVar('T')


# ---

class CalculationStrategy(Generic[T], Strategy[T]):
    def __init__(self, numbers: Iterable[T]):
        self._numbers = numbers

    @abstractmethod
    def doAlgorithm(self) -> T:
        pass


# ### Addition

class AdditionStrategy(Generic[T], CalculationStrategy[T]):
    def __init__(self, numbers: Iterable[T]):
        super().__init__(numbers)

    def doAlgorithm(self) -> T:
        if not self._numbers:
            return 0
            
        return sum(self._numbers)

    def __str__(self) -> str:
        return  ' + '.join(map(str, self._numbers))


# #### Result

# + active=""
# print(AdditionStrategy([1, 2]).doAlgorithm())
# -

# #### ToString

# + active=""
# print(AdditionStrategy((2, 2, 3)))
# -

# ### Multiplication

class MultiplicationStrategy(Generic[T], CalculationStrategy[T]):
    def __init__(self, numbers: Iterable[T]):
        super().__init__(numbers)

    def doAlgorithm(self) -> T:
        return reduce(lambda acc, number: acc * number, self._numbers)

    def __str__(self) -> str:
        return ' x '.join(map(str, self._numbers))


# #### Result

# + active=""
# print(MultiplicationStrategy((2, 3)).doAlgorithm())
# -

# #### ToString

# + active=""
# print(MultiplicationStrategy((2, 2, 3)))
# -

class CalculationStrategyFactory(ABC, Generic[T]):
    @staticmethod
    def createAdditionStrategy(numbers: Iterable[T]) -> CalculationStrategy[T]:
        return AdditionStrategy(numbers)

    @staticmethod
    def createAdditionStrategies(numbersCollection: Iterable[Iterable[T]]) -> Iterable[CalculationStrategy[T]]:
        return [CalculationStrategyFactory.createAdditionStrategy(numbers) for numbers in numbersCollection]

    @staticmethod
    def createMultiplicationStrategy(numbers: Iterable[T]) -> CalculationStrategy[T]:
        return MultiplicationStrategy(numbers)

    @staticmethod
    def createMultiplicationStrategy(numbersCollection: Iterable[Iterable[T]]) -> Iterable[CalculationStrategy[T]]:
        return [CalculationStrategyFactory.createMultiplicationStrategy(numbers) for numbers in numbersCollection]
