from ..strategies.strategy import Strategy


class StrategyContext:

    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def prepareAndDoAlgorithm(self) -> any:
        return self._strategy.doAlgorithm()

    @staticmethod
    def getInput():
        return input
