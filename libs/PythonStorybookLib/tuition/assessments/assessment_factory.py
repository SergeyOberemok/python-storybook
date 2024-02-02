from .assessment import Assessment
from ..contexts.strategy_context import StrategyContext
from ..contexts.survey_context_strategy_factory import SurveyContextStrategyFactory
from ..strategies.add_strategy import AddStrategy


class AssessmentFactory(object):
    @staticmethod
    def createAdditionAssessment(numbersAndQuestions: list) -> Assessment:
        def createQuestion(x: int, y: int, question: str) -> StrategyContext:
            strategy = AddStrategy[int]((x, y))
            strategyContext = SurveyContextStrategyFactory.create(strategy, question)

            return strategyContext

        questions = [createQuestion(x, y, question) for (x, y, question, *tail) in numbersAndQuestions]

        return Assessment(questions)

    @staticmethod
    def createMultiplyAssessment(numbers: list, count: int = 0) -> Assessment:
        pass
        # def getQuestion() -> StrategyContext:
        #    x, y = getItemsRandomly(numbers, 2)

        #    strategy = MultiplyStrategy((x, y))
        #    return SurveyContextStrategyFactory.create(strategy)

        # return AssessmentFactory.create(getQuestion, count)
