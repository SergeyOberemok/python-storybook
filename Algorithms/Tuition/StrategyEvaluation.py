# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python [conda env:base] *
#     language: python
#     name: conda-base-py
# ---

# +
from collections.abc import Callable, Iterable
from typing import TypeVar, Generic

from Strategies import Strategy, AdditionStrategy, CalculationStrategyFactory
from Evaluation import Evaluation
# -

# ---

T = TypeVar('T')


# ---

# ### Definition

class StrategyEvaluation(Generic[T], Evaluation[T]):
    def __init__(self, strategy: Strategy[T]):
        self._strategy = strategy

    def __str__(self) -> str:
        return str(self._strategy)

    @property
    def answer(self) -> T:
        pass

    @property
    def target(self) -> T:
        return self._strategy.doAlgorithm()

    def evaluate(self) -> Iterable[str, T, T, bool]:
        target = self.target
        answer = self.answer
        result = answer == target

        return str(self), target, answer, result
