import random
from typing import Callable
from ..contexts.strategy_context import StrategyContext


class Assessment:
    def __init__(self, questions: list[StrategyContext]):
        random.shuffle(questions)

        self._questions = questions

    def start(self) -> bool:
        result = True

        for question in self._questions:
            if question.prepareAndDoAlgorithm():
                print('Correct')
            else:
                print('Wrong')
                result = False

        return result