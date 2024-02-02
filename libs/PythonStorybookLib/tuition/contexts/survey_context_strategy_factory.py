from .strategy_context import StrategyContext
from .survey_context_strategy import SurveyContextStrategy
from ..strategies.strategy import Strategy


class SurveyContextStrategyFactory:
    @staticmethod
    def create(strategy: Strategy, question: str) -> StrategyContext:
        return SurveyContextStrategy(strategy, question)
