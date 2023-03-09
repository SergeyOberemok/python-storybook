
from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def doAction(self, question: str, answerToQuestion: int) -> bool:
        pass
