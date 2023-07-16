# 必要なモジュールをインポートします。
# FlaskはPythonの軽量なウェブフレームワークで、
# これを使ってウェブアプリケーションを作成します。
from flask import Flask,Blueprint, render_template, request, jsonify, g
from flask_socketio import SocketIO
import sqlite3

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

# データベースへの接続を取得または作成
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('chat.db')
        g.db.row_factory = sqlite3.Row
    return g.db

# データベースの接続を閉じる
@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# データベースを初期化する関数
def init_db():
    con = sqlite3.connect('chat.db')
    con.execute("DROP TABLE IF EXISTS USERS")
    con.execute("""
    CREATE TABLE USERS (
        user_id INTEGER PRIMARY KEY, 
        name TEXT, 
        email TEXT UNIQUE, 
        img TEXT, 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
        deleted_at TIMESTAMP
    )
    """)
    con.execute("DROP TABLE IF EXISTS MESSAGES")
    con.execute("""
    CREATE TABLE MESSAGES (
        message_id INTEGER PRIMARY KEY, 
        user_id INTEGER,
        message TEXT, 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
        delete_flag BOOLEAN DEFAULT 0,
        FOREIGN KEY(user_id) REFERENCES USERS(user_id)
    )
    """)
    con.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login' , methods=['GET'])
def login():
    return "<p>Hello World!</p>"
#    return login.login()

@app.route('/login' , methods=['POST'])
def login():
   return auth.login()

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return chat.handle_chat()


if __name__ == "__main__":
    init_db()  # データベースを初期化する
    socketio.run(app)