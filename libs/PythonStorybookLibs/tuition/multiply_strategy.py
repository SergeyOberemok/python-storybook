
from survey_strategy import SurveyStrategy

class MultiplyStrategy(SurveyStrategy):

    def __init__(self, data: tuple) -> None:
        super().__init__()

        self.data = data

    def doAction(self, question: str, answerToQuestion: int) -> bool:
        question = '%s equals to ' %question

        return super().doAction(question, answerToQuestion)