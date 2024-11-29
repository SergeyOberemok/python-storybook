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

from Strategies import Strategy
import random


# ---

# ### Basic

class Assessment:
    def __init__(self, questions: list[Strategy]):
        random.shuffle(questions)

        self._questions = questions

    def start(self) -> bool:
        result = map(lambda question: question.doAlgorithm(), self._questions)
        
        return all(result)


# ### Factory

class AssessmentFactory(object):
    @staticmethod
    def createAdditionAssessment(params: list[tuple[int, int, str]]) -> Assessment:
        def createQuestion(x: int, y: int, question: str) -> StrategyContext:
            strategy = AdditionStrategy[int]((x, y))
            strategyContext = SurveyContextStrategyFactory.create(strategy, question)

            return strategyContext

        questions = [createQuestion(x, y, question) for (x, y, question) in params]

        return Assessment(questions)

    @staticmethod
    def createMultiplyAssessment(numbers: list, count: int = 0) -> Assessment:
        pass
        # def getQuestion() -> StrategyContext:
        #    x, y = getItemsRandomly(numbers, 2)

        #    strategy = MultiplyStrategy((x, y))
        #    return SurveyContextStrategyFactory.create(strategy)

        # return AssessmentFactory.create(getQuestion, count)
