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

from collections.abc import Iterable, Callable

from Assessment import AssessmentCollection
from Strategy import Strategy
from Strategies import AdditionStrategy
from StrategyEvaluation import StrategyEvaluation
from StrategyEvaluations import StrategyEvaluationFactory


# ### Survey assessment

# + active=""
# def getAnswer(message: str) -> int:
#     return int(input(f'What is {message}'))
#     
# assessment = AssessmentCollection([
#     StrategyEvaluationFactory.createSurveyStrategyEvaluation(AdditionStrategy((2, 2)))
# ]).pipe(lambda item: item.setAnswer(getAnswer))
#
# print(assessment.assist(), assessment)
# -

# ### Response assessment

# + active=""
# assessment = AssessmentCollection([
#     StrategyEvaluationFactory.createResponseStrategyEvaluation(AdditionStrategy((2, 2)))
# ])
#
# for item in assessment:
#     item.pipe(lambda i: i.setAnswer(lambda: 3)).assist()
#
# print(assessment.assist(), assessment.pipe(lambda i: i.setAnswer(lambda: 4)).assist(), assessment)
# -

class AssessmentFactory:
    @staticmethod
    def createSurveyAssessment(strategies: Iterable[Strategy], getAnswer: Callable):
        strategies = map(StrategyEvaluationFactory.createSurveyStrategyEvaluation, strategies)
        assessment =  AssessmentCollection(strategies).pipe(lambda item: item.setAnswer(getAnswer))

        return assessment

    @staticmethod
    def createResponseAssessment(strategies: Iterable[Strategy]):
        strategies = map(StrategyEvaluationFactory.createResponseStrategyEvaluation, strategies)
        return AssessmentCollection(strategies)
