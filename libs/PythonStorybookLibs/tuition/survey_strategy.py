
from strategy import Strategy

class SurveyStrategy(Strategy):

    def doAction(self, question: str, answerToQuestion: int) -> bool:
        answer = input(question)

        return answerToQuestion == answer