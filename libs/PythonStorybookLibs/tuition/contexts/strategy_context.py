
from ..strategies.strategy import Strategy

class StrategyContext:
    
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def prepareAndDoAlgorithm(self) -> bool:
        self._strategy.doAlgorithm()

        return True;

    def getInput():
        return input