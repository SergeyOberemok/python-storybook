from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, debug=True, cors_allowed_origins='*', async_mode='eventlet')


@socketio.on('assess')
def handle_assess(answer: str):
    result = 4

    send('Success' if result == int(answer) else 'Fail')


@socketio.on('question')
def handle_question(args):
    message = '2 + 2'

    send(message)


if __name__ == '__main__':
    socketio.run(app)
