from .strategy_context import StrategyContext
from ..strategies.strategy import Strategy


class SurveyContextStrategy(StrategyContext):
    def __init__(self, strategy: Strategy, question: str):
        super().__init__(strategy)

        self.question = question

    def prepareAndDoAlgorithm(self) -> tuple[bool, any]:
        inputMethod = StrategyContext.getInput()

        response = inputMethod(self.question)

        if not response:
            raise Exception('Response is empty')

        answer = self.strategy.doAlgorithm()

        return str(answer) == response, answer
