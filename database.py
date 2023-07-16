import sqlite3  # SQLiteを操作するためのモジュールをインポート
from flask import g  # Flaskのグローバル変数gを使用

# データベースへの接続を取得または作成
def get_db():
    # gオブジェクトにデータベース接続が存在しない場合
    if 'db' not in g:
        # SQLiteに接続し、接続オブジェクトを作成
        g.db = sqlite3.connect('chat.db')
        # row_factoryにsqlite3.Rowを設定し、データベースから取得した行を辞書のように扱えるようにする
        g.db.row_factory = sqlite3.Row
    return g.db  # データベース接続オブジェクトを返す

# データベースの接続を閉じる
def close_db(exception=None):
    # gオブジェクトからデータベース接続を取り出す。データベース接続が存在しない場合はNoneを返す。
    db = g.pop('db', None)

    # データベース接続が存在する場合
    if db is not None:
        db.close()  # データベースの接続を閉じる

# データベースを初期化する関数
def init_db():
    # SQLiteに接続し、接続オブジェクトを作成
    con = sqlite3.connect('chat.db')

    # USERSテーブルが存在する場合、それを削除する
    con.execute("DROP TABLE IF EXISTS USERS")

    # USERSテーブルを作成する
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

    # MESSAGESテーブルが存在する場合、それを削除する
    con.execute("DROP TABLE IF EXISTS MESSAGES")

    # MESSAGESテーブルを作成する
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





# このスクリプトがコマンドラインから実行された場合にだけ、データベースの初期化を行う
if __name__ == '__main__':
    init_db()  # データベースを初期化する
