
import random
from .strategy_context import StrategyContext

class Assessment:
    def __init__(self, questions: list[StrategyContext]) -> None:
        random.shuffle(questions)

        self._questions = questions

    def start(self):
        for question in self._questions:
            if question.prepareAndDoAlgorithm():
                print('Correct')
            else:
                print('Wrong')
