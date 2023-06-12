
from typing import Callable
import pytest
from tuition.contexts.strategy_context import StrategyContext
from tuition.strategies.multiply_strategy import MultiplyStrategy
from tuition.strategies.strategy import Strategy
from tuition.contexts.survey_context_strategy_factory import (
    SurveyContextStrategyFactory,
)


@pytest.fixture
def strategy() -> Strategy:
    num1 = 2
    num2 = 3

    return MultiplyStrategy((num1, num2))


@pytest.fixture
def question(strategy: Strategy[int]) -> str:
    return str(strategy)


@pytest.fixture
def answer(strategy: Strategy[int]) -> str:
    return str(strategy.doAlgorithm())


@pytest.fixture
def getInput(question: str, answer: str) -> Callable:
    def inputMock(q: str) -> str:
        assert question == q
        return answer

    def getInputMock() -> Callable:
        return inputMock

    return getInputMock


class TestSurveyContextStrategy:
    def test_prepareAndDoAlgorithm(
        self,
        monkeypatch,
        strategy: Strategy,
        question: str,
        answer: int,
        getInput: Callable
    ) -> None:
        monkeypatch.setattr(StrategyContext, "getInput", getInput)

        survey = SurveyContextStrategyFactory.create(strategy, question)

        assert survey.prepareAndDoAlgorithm() == True