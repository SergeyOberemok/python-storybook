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

from collections.abc import Iterable, Iterator

from Strategies import Strategy


# ## Evaluation

class StrategiesEvaluation:
    def __init__(self, strategies: Iterable[Strategy]):
        self._strategies = strategies
        self._iterator = None
        self._item = None

    def __iter__(self):
        self._iterator = iter(self._strategies)

        return self

    def __next__(self):
        self._item = next(self._iterator)

        return (str(self._item), self._item.doAlgorithm())

    def evaluate(self) -> Iterable:
        return [values for values in self._strategies]
