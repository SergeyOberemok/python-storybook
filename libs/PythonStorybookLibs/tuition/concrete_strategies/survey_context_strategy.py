
from ..strategy_context import StrategyContext
from ..strategy import Strategy

class SurveyContextStrategy(StrategyContext):

    def __init__(self, question: str, strategy: Strategy) -> None:
        super().__init__(strategy)

        self._question = question

    def prepareAndDoAlgorithm(self) -> bool:
        response = input('%s: ' %self._question)

        answer = self.strategy.doAlgorithm()

        return str(answer) == response
