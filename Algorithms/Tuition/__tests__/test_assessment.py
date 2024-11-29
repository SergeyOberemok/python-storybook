from pytest import mark

from Assessment import AssessmentFactory, Assessment
from Strategies import Strategy, AdditionStrategy


@mark.parametrize("numbersAndQuestions", [[(1, 1, "1+1", "2"), (2, 3, "2+3", "5")]])
def test_start_old(self, monkeypatch, numbersAndQuestions: list):
    pass

    def inputMock(q: str) -> str:
        (*numbersAndQuestion, answer) = next(
            x for x in numbersAndQuestions if x[2] == q
        )

        return answer

    def getInputMock():
        return inputMock

    monkeypatch.setattr(Strategy, "getInput", getInputMock)

    assessment = AssessmentFactory.createAdditionAssessment(numbersAndQuestions)

    assert assessment.start() is True


def test_start(monkeypatch):
    monkeypatch.setattr(AdditionStrategy, 'doAlgorithm', lambda _: True)

    assessment = Assessment([AdditionStrategy()])

    result = assessment.start()

    assert result
