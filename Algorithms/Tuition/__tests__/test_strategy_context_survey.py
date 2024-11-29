import pytest

from Strategies import MultiplicationStrategy
from StrategyContext import StrategyContext, SurveyContextStrategyFactory, SurveyContextStrategy


@pytest.fixture
def question() -> str:
    return 'What is'


def test_strategy_context(monkeypatch):
    monkeypatch.setattr(MultiplicationStrategy, 'doAlgorithm', lambda _: True)

    strategy = MultiplicationStrategy()
    strategyContext = StrategyContext(strategy)
    result = strategyContext.doAlgorithm()

    assert result is True
    assert str(strategyContext) == str(strategy)


def test_doAlgorithm():
    strategy = MultiplicationStrategy()
    answer = strategy.doAlgorithm()
    survey = SurveyContextStrategy(strategy, lambda: answer)

    result = survey.doAlgorithm()

    assert result
