
import pytest
from pytest import mark
from tuition.assessments.assessment_factory import AssessmentFactory
from tuition.contexts.strategy_context import StrategyContext


class TestAssessment:
    @mark.parametrize("numbersAndQuestions", [[(1, 1, "1+1", "2"), (2, 3, "2+3", "5")]])
    def test_start(self, monkeypatch, numbersAndQuestions: list) -> None:
        def inputMock(q: str) -> str:
            (*numbersAndQuestion, answer) = next(
                x for x in numbersAndQuestions if x[2] == q
            )

            return answer

        def getInputMock():
            return inputMock

        monkeypatch.setattr(StrategyContext, "getInput", getInputMock)

        assessment = AssessmentFactory.createAdditionAssessment(numbersAndQuestions)

        assert assessment.start() == True
