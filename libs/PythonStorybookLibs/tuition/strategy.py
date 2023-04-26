
from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def doAlgorithm(self) -> bool:
        pass
