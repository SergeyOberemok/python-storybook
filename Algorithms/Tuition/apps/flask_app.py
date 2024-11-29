from flask import Flask
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
socketio = SocketIO(app, debug=True, cors_allowed_origins='*', async_mode='eventlet')

numbers = range(3)
numbersIterator = iter(numbers)


@app.route('/')
def hello_world():
    return 'hello world'


@socketio.on('my_event')
def check_sockets(data: str):
    multiplier = 0 if data is None else int(data)

    try:
        i = next(numbersIterator)
        result = i * multiplier

        emit('server', {'data': result})
    except StopIteration:
        emit('server', {'data': 'empty'})

    send(data)


if __name__ == '__main__':
    socketio.run(app)
