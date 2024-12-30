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

# + editable=true slideshow={"slide_type": ""}
from collections.abc import Iterable, Callable
# -

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
# for i in [assessment.assess(), assessment, assessment.results, assessment.result]:
#     print(i)
# -

# ### Response assessment

# + active=""
# assessment = AssessmentCollection([
#     StrategyEvaluationFactory.createResponseStrategyEvaluation(AdditionStrategy((2, 2)))
# ])
#
# for item in assessment:
#     item.pipe(lambda i: i.setAnswer(lambda: 3)).assess()
#
# for i in [assessment.assess(), assessment, assessment.results, assessment.result]:
#     print(i)
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
