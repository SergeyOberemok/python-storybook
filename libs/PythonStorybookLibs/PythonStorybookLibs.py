
from tuition.assessment import Assessment
from tuition.strategy_context import StrategyContext
from tuition.concrete_strategies.survey_context_strategy import SurveyContextStrategy
from tuition.concrete_strategies.multiply_strategy import MultiplyStrategy
from tuition.concrete_strategies.add_strategy import AddStrategy

questions: list[StrategyContext] = [
    SurveyContextStrategy(
        "What is the result of multiplying 2 and 2", MultiplyStrategy[int]((2, 2))
    ),
    SurveyContextStrategy(
        "What is the result of adding 2 and 3", AddStrategy[int]((2, 3))
    ),
]

assessment = Assessment(questions)

assessment.start()