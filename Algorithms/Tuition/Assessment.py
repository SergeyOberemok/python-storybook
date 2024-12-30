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

from abc import ABC, abstractmethod
from collections.abc import Iterable, Callable

from StrategyEvaluation import StrategyEvaluation


# ---

# ### Definition

class Assessment(ABC):
    @abstractmethod
    def pipe(self, *funcs):
        pass

    @abstractmethod
    def assess(self):
        pass


# ## Concrete

# ### Item

class AssessmentItem(Assessment):
    def __init__(self, question: StrategyEvaluation):
        self._question = question

    def __str__(self) -> str:
        return str(self._question)

    @property
    def goal(self):
        return self._question.target

    def pipe(self, *funcs):
        for func in funcs:
            self._question = func(self._question)

        return self

    def assess(self):
        return self._question.evaluate()


# ### Collection

class AssessmentCollection(Assessment):
    def __init__(self, questions: Iterable[StrategyEvaluation]):
        self._questions = [AssessmentItem(question) for question in questions]
        self._pipeFuncs = []
        self._iterator = None

    def __iter__(self):
        self._iterator = iter(self._questions)
        
        return self

    def __next__(self):
        return next(self._iterator)

    def __str__(self):
        return '\n'.join([str(question) for question in self._questions])

    @property
    def results(self):
        return [question.assess() for question in self._questions]

    @property
    def result(self):
        return all(value for *head, value in self.results)

    def pipe(self, *funcs):
        self._pipeFuncs = funcs
        
        return self

    def assess(self) -> bool:
        for question in self._questions:
            question.pipe(*self._pipeFuncs).assess()
                
        return self.result
