from typing import Callable

import pytest

from tuition.contexts.strategy_context import StrategyContext
from tuition.contexts.survey_context_strategy_factory import (
    SurveyContextStrategyFactory,
)
from tuition.strategies.multiply_strategy import MultiplyStrategy
from tuition.strategies.strategy import Strategy


@pytest.fixture
def strategy() -> Strategy:
    num1 = 2
    num2 = 3

    return MultiplyStrategy((num1, num2))


@pytest.fixture
def question(strategy: Strategy[int]) -> str:
    return str(strategy)


@pytest.fixture
def answer(strategy: Strategy[int]) -> int:
    return strategy.doAlgorithm()


@pytest.fixture
def getInput(question: str, answer: int) -> Callable:
    def inputMock(q: str) -> str:
        assert question == q
        return str(answer)

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
    ):
        monkeypatch.setattr(StrategyContext, "getInput", getInput)

        survey = SurveyContextStrategyFactory.create(strategy, question)

        result, expected = survey.prepareAndDoAlgorithm()

        assert result is True
        assert answer == expected
