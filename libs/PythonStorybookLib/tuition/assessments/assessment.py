import random
from typing import Callable

from ..contexts.strategy_context import StrategyContext


class Assessment:
    def __init__(self, questions: list[StrategyContext]):
        random.shuffle(questions)

        self._questions = questions

    def start(self, mapAnswer: Callable = None) -> bool:
        result = True

        for question in self._questions:
            try:
                isCorrect, expected = question.prepareAndDoAlgorithm()

                if mapAnswer is not None:
                    expected = mapAnswer(expected)

                if isCorrect:
                    print('Correct - %s' % expected)
                else:
                    print('Wrong, correct answer is %s' % expected)
                    result = False
            except:
                return False

        return result
