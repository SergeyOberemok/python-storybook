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
from collections.abc import Iterable, Callable

from StrategyEvaluation import StrategyEvaluation


# ---

# ### Definition

class Assessment(ABC):
    @abstractmethod
    def pipe(self, *funcs):
        pass

    @abstractmethod
    def assist(self):
        pass


# ## Concrete

# ### Item

class AssessmentItem(Assessment):
    def __init__(self, question: StrategyEvaluation, assistCb: Callable = None):
        self._question = question
        self._assistCb = assistCb

    def __str__(self) -> str:
        return str(self._question)

    def pipe(self, *funcs):
        for func in funcs:
            self._question = func(self._question)

        return self

    def assist(self):
        result = self._question.evaluate()

        if self._assistCb:
            self._assistCb(result)

        return result


# ### Collection

class AssessmentCollection(Assessment):
    def __init__(self, questions: Iterable[StrategyEvaluation]):
        self._questions = questions
        self.__reset()
        self._pipeFuncs = []

    def __iter__(self):
        self.__reset()
        self._iterator = iter(self._questions)
        
        return self

    def __next__(self):
        try:
            self._question = next(self._iterator)

            return AssessmentItem(self._question, lambda result: self._results.append(result))
        except StopIteration:
            self._iterator = None
            raise StopIteration

    def __str__(self):
        return '\n'.join([', '.join(map(str, items)) for items in self._results])

    def pipe(self, *funcs):
        self._pipeFuncs = funcs
        
        return self

    def assist(self) -> bool:
        if not self._iterator:
            for item in self:
                item.pipe(*self._pipeFuncs).assist()
                
        return all(value for *head, value in self._results)

    def __reset(self):
        self._iterator = None
        self._results = []
