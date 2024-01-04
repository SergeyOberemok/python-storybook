
from typing import Callable
from .strategy_context import StrategyContext
from ..strategies.strategy import Strategy


class SurveyContextStrategy(StrategyContext):
    def __init__(self, strategy: Strategy, question: str):
        super().__init__(strategy)

        self.question = question

    def prepareAndDoAlgorithm(self) -> bool:
        inputMethod = StrategyContext.getInput()

        response = inputMethod(self.question)

        answer = self.strategy.doAlgorithm()

        return str(answer) == response