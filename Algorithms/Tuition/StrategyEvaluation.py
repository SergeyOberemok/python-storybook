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

    @property
    def answer(self) -> T:
        pass

    def evaluate(self) -> Iterable[T, T, bool]:
        target = self._strategy.doAlgorithm()
        answer = self.answer
        result = answer == target

        return target, answer, result

    def __str__(self) -> str:
        return str(self._strategy)
