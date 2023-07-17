# 必要なモジュールをインポートします。
# FlaskはPythonの軽量なウェブフレームワークで、
# これを使ってウェブアプリケーションを作成します。
from flask import Flask,Blueprint, render_template, request, jsonify, g
from flask_socketio import SocketIO
import sqlite3
import secrets
# flask_socketioは、Flaskと統合されたSocket.IOのライブラリで、
# サーバとクライアント間のリアルタイム通信を可能にします。
from flask_socketio import SocketIO, emit
from application.login import auth
from application.chat import chat



def generate_secret_key():
    return secrets.token_hex(16)

# Flaskのアプリケーションインスタンスを作成します。
# これは、ウェブアプリケーション全体を制御する中心的なオブジェクトです。
app = Flask(__name__)
app.secret_key =  generate_secret_key()
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
        password TEXT,
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




if __name__ == "__main__":
    #init_db()  # データベースを初期化する
    app.run(debug=True)