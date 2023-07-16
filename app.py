# 必要なモジュールをインポートします。
# FlaskはPythonの軽量なウェブフレームワークで、
# これを使ってウェブアプリケーションを作成します。
from flask import Flask, render_template


# flask_socketioは、Flaskと統合されたSocket.IOのライブラリで、
# サーバとクライアント間のリアルタイム通信を可能にします。
from flask_socketio import SocketIO, emit
from components.login import auth
from components.chat import chat


# Flaskのアプリケーションインスタンスを作成します。
# これは、ウェブアプリケーション全体を制御する中心的なオブジェクトです。
app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(chat)

# SocketIO インスタンスを作成
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login' , methods=['POST'])
def login():
    return login.login()

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return chat.handle_chat()


if __name__ == "__main__":
    socketio.run(app)