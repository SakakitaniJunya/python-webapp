# 必要なモジュールをインポートします。
# FlaskはPythonの軽量なウェブフレームワークで、
# これを使ってウェブアプリケーションを作成します。
from flask import Flask, render_template

# flask_socketioは、Flaskと統合されたSocket.IOのライブラリで、
# サーバとクライアント間のリアルタイム通信を可能にします。
from flask_socketio import SocketIO, emit

# Flaskのアプリケーションインスタンスを作成します。
# これは、ウェブアプリケーション全体を制御する中心的なオブジェクトです。
app = Flask(__name__)

# SocketIOのインスタンスを作成し、Flaskアプリケーションに統合します。
socketio = SocketIO(app)

# ユーザーから受信したメッセージを保存するリストを作成します。
# 新しいメッセージが来るたびに、このリストに追加されます。
messages = []

# Flaskのルートデコレータを使用して、ウェブページのエンドポイント（URL）を作成します。
# この例では、サイトのホームページ（"/"）を作成しています。
@app.route('/')
def index():
    # index.htmlを表示します。これがユーザーに見せるウェブページです。
    # さらに、保存してあるメッセージをこのページに渡します。
    return render_template('index.html', messages=messages)

# Socket.IOのイベントリスナーを作成します。"message"という名前のイベントを待ち受けます。
# クライアントから"message"イベントが送られてくると、この関数が自動的に呼び出されます。
@socketio.on('message')
def handle_message(data):
    # ユーザーから送られてきたデータ（メッセージ）をmessagesリストに追加します。
    messages.append(data)
    # emit関数を使って、"message"イベントを送信します。dataをそのまま送ります。
    # ここでのbroadcast=Trueは、接続しているすべてのクライアントにイベントを送るという意味です。
    emit('message', data, broadcast=True)

# このスクリプトが直接実行されたとき（例えば、python app.pyのように）、
# Flaskサーバーを起動します。引数にFlaskアプリケーションを渡します。
# （このスクリプトが他のスクリプトからインポートされたときはサーバーは起動されません）
if __name__ == '__main__':
    socketio.run(app)
