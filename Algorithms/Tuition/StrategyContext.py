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

# +
from abc import ABC
from typing import TypeVar, Generic, Callable

from Strategies import Strategy, AdditionStrategy
# -

# ---

T = TypeVar('T')


# ---

# ### Definition

class StrategyContext(Generic[T], Strategy[T]):
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def doAlgorithm(self) -> T:
        return self._strategy.doAlgorithm()

    def __str__(self) -> str:
        return str(self._strategy)


# ### Survey

class SurveyContextStrategy(StrategyContext[str]):
    def __init__(self, strategy: Strategy, answerObtainer: Callable):
        super().__init__(strategy)

        self.obtainAnswer = answerObtainer

    def doAlgorithm(self) -> str:
        response = self.obtainAnswer()
        result = self.strategy.doAlgorithm()

        return 'Success' if result == response else 'Failure'


# + active=""
# print(SurveyContextStrategy(AdditionStrategy((2, 2)), lambda: int(input('What is the outcome of'))).doAlgorithm())
# -

# ### Factory

class SurveyContextStrategyFactory(ABC):
    @staticmethod
    def create(strategy: Strategy, question: str = 'What is the outcome of') -> StrategyContext:
        return SurveyContextStrategy(strategy, lambda: int(input(question)))

# + active=""
# print(SurveyContextStrategyFactory.create(AdditionStrategy()).doAlgorithm())
