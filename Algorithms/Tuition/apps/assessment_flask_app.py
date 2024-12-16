from flask import Flask
from flask_socketio import SocketIO, send
import os, sys

from Strategies import CalculationStrategyFactory

directoryPaths = [
    os.path.abspath(os.path.join('..\\..\\..\\Math\\math_lib'))
]

for directoryPath in (directoryPath for directoryPath in directoryPaths if directoryPath not in sys.path):
    sys.path.append(directoryPath)

import numbers_utils

from Assessments import AssessmentFactory

app = Flask(__name__)
socketio = SocketIO(app, debug=True, cors_allowed_origins='*', async_mode='eventlet')

numbersPairs = numbers_utils.generateRandomNumbersPairs(maxNumber=10, count=3)
strategies = CalculationStrategyFactory.createAdditionStrategies(numbersPairs)
assessment = AssessmentFactory.createResponseAssessment(strategies)
assessmentIterator = iter(assessment)
assessmentItem = None


@socketio.on('assess')
def handle_assess(answer: str):
    result = assessmentItem.pipe(lambda item: item.setAnswer(lambda: int(answer))).assist()

    send(result)


@socketio.on('question')
def handle_question(args):
    global assessmentItem

    try:
        assessmentItem = next(assessmentIterator)

        send(str(assessmentItem))
    except StopIteration:
        send(str(assessment))




if __name__ == '__main__':
    socketio.run(app)
