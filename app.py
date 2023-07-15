from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# メッセージを保存しておくリスト
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@socketio.on('message')
def handle_message(data):
    # 受信したメッセージを保存
    messages.append(data)
    # 全てのクライアントにメッセージを送信
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
