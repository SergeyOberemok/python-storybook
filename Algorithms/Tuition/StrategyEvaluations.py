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

from typing import Generic, TypeVar
from collections.abc import Callable

from Strategy import Strategy
from StrategyEvaluation import StrategyEvaluation
from Strategies import AdditionStrategy

# ---

T = TypeVar('T')


# ## Get answer

# ### Survey

class SurveyStrategyEvaluation(Generic[T], StrategyEvaluation[T]):
    def __init__(self, strategy: Strategy[T], answerObtainer: Callable[[str], T] = None):
        super().__init__(strategy)

        self._obtainAnswer = answerObtainer

    def setAnswer(self, answerObtainer: Callable[[str], T]):
        self._obtainAnswer = answerObtainer

        return self

    @property
    def answer(self) -> T:
        return self._obtainAnswer(str(self)) if self._obtainAnswer else None


# + active=""
# print(SurveyStrategyEvaluation(AdditionStrategy((2, 2)), lambda question: int(input(question))).evaluate())

# + active=""
# print(SurveyStrategyEvaluation(AdditionStrategy((2, 2))).setAnswer(lambda question: int(input(question))).evaluate())
# -

# ### Response

class ResponseStrategyEvaluation(Generic[T], StrategyEvaluation[T]):
    def __init__(self, strategy: Strategy[T], answerObtainer: Callable[[], T] = None):
        super().__init__(strategy)

        self._obtainAnswer = answerObtainer

    def setAnswer(self, answerObtainer: Callable[[], T]):
        self._obtainAnswer = answerObtainer

        return self

    @property
    def answer(self) -> T:
        return self._obtainAnswer() if self._obtainAnswer else None


# + active=""
# print(ResponseStrategyEvaluation(AdditionStrategy((2, 2)), lambda: 3).evaluate())

# + active=""
# print(ResponseStrategyEvaluation(AdditionStrategy((2 ,2))).setAnswer(lambda: 3).evaluate())
# -

# ### Factory

class StrategyEvaluationFactory:
    @staticmethod
    def createSurveyStrategyEvaluation(strategy: Strategy[T]) -> StrategyEvaluation[T]:
        return SurveyStrategyEvaluation(strategy, lambda question: int(input(question)))

    @staticmethod
    def createResponseStrategyEvaluation(strategy: Strategy[T]) -> StrategyEvaluation[T]:
        return ResponseStrategyEvaluation(strategy)

# + active=""
# print(StrategyEvaluationFactory.createSurveyStrategyEvaluation(AdditionStrategy((2, 2))).evaluate())

# + active=""
# print(StrategyEvaluationFactory.createResponseStrategyEvaluation(AdditionStrategy((2, 2))).setAnswer(lambda: 3).evaluate())
