from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class Strategy(ABC, Generic[T]):
    @abstractmethod
    def doAlgorithm(self) -> T:
        pass
