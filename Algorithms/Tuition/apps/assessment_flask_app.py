import os
import sys

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from Strategies import CalculationStrategyFactory

directoryPaths = [
    os.path.abspath(os.path.join('..\\..\\..\\Math\\math_lib'))
]

for directoryPath in (directoryPath for directoryPath in directoryPaths if directoryPath not in sys.path):
    sys.path.append(directoryPath)

import numbers_utils

from Assessments import AssessmentFactory

app = Flask(__name__, template_folder='dist', static_folder='dist', static_url_path='/')
socketio = SocketIO(app, debug=True, cors_allowed_origins='*', async_mode='eventlet')

assessment = None
assessmentIterator = None
assessmentItem = None


def start_assessment(quantity: int):
    numbersPairs = numbers_utils.generateRandomNumbersPairs(maxNumber=10, count=quantity)
    strategies = CalculationStrategyFactory.createAdditionStrategies(numbersPairs)

    assessment = AssessmentFactory.createResponseAssessment(strategies)
    assessmentIterator = iter(assessment)

    return assessment, assessmentIterator


@socketio.on('start')
def handle_start(quantity: int):
    global assessment, assessmentIterator

    assessment, assessmentIterator = start_assessment(quantity)


@socketio.on('objective')
def handle_objective(args):
    return assessmentItem.goal


@socketio.on('assess')
def handle_assess(answer: str):
    result = assessmentItem.pipe(lambda item: item.setAnswer(lambda: int(answer))).assess()

    return result


@socketio.on('question')
def handle_question(args):
    global assessmentItem

    try:
        assessmentItem = next(assessmentIterator)

        return str(assessmentItem)
    except StopIteration:
        emit('end', {'assessment': str(assessment), 'results': assessment.results, 'result': assessment.result})
        return ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping')
def pong_hello_world():
    return 'pong hello world'


@app.route('/image/<int:digit>')
def fetch_image(digit: int):
    return f'{digit}'


if __name__ == '__main__':
    socketio.run(app)
