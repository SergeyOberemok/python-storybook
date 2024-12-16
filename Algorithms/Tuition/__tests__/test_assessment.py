from pytest import mark

from Assessment import AssessmentFactory, Assessment
from Strategies import Strategy, AdditionStrategy
from StrategyContext import SurveyContextStrategy


@mark.parametrize("numbersAndQuestions", [[(1, 1, "1+1", "2"), (2, 3, "2+3", "5")]])
def test_start_old(monkeypatch, numbersAndQuestions: list):
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


def test_assessment_start(monkeypatch):
    monkeypatch.setattr(AdditionStrategy, 'doAlgorithm', lambda _: True)

    assessment = Assessment([AdditionStrategy()])

    result = assessment.start()

    assert result


@mark.parametrize("numbersAndQuestions", [[(1, 1, 2, "1+1"), (2, 3, 5, "2+3")]])
def test_assessment_start_with_params(numbersAndQuestions):
    strategies = [SurveyContextStrategy(AdditionStrategy((one, two)), lambda: prompt) for one, two, prompt, *rest in
                  numbersAndQuestions]
    assessment = Assessment(strategies)

    result = assessment.start()

    assert result
