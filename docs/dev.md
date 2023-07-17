以下に、推奨されるFlaskのルーティング設定に従ったファイルの実装例を示します。

1. `application/models/chat.py`:
```python
from application import db

class Message(db.Model):
    __tablename__ = 'messages'

    message_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Message {self.message}>'
```

2. `application/models/login.py`:
```python
from application import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'
```

3. `application/views/__init__.py`:
```python
from flask import Blueprint

bp = Blueprint('views', __name__)

from application.views import login, chat
```

4. `application/views/chat.py`:
```python
from flask import render_template, request, jsonify
from application.models.chat import Message
from application import db

@bp.route('/chat', methods=['POST'])
def post_message():
    message = request.json['message']
    user_id = session.get('user_id')
    
    new_message = Message(message=message, user_id=user_id)
    db.session.add(new_message)
    db.session.commit()

    return jsonify(success=True)

@bp.route('/chat', methods=['GET'])
def chat_page():
    return render_template('chat.html')

@bp.route('/get_messages', methods=['GET'])
def get_messages():
    user_id = session.get('user_id')

    user_messages = Message.query.filter_by(user_id=user_id).all()
    all_messages = Message.query.all()

    user_message_list = [{'message': m.message, 'user_id': m.user_id} for m in user_messages]
    all_messages_list = [{'message': m.message, 'user_id': m.user_id} for m in all_messages]

    return jsonify(user_message_list=user_message_list, all_messages_list=all_messages_list)
```

5. `application/views/login.py`:
```python
from flask import Blueprint, render_template, request, jsonify, session
from application.models.login import User
from application import db

@bp.route('/login', methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email, password=password).first()

    if user is not None:
        session['user_id'] = user.user_id
        session['email'] = user.email
        session['user_name'] = user.name
        response = {
            "status": "success",
            "message": "Login Success: " + email
        }
        return jsonify(response), 200
    else:
        response = {
            "status": "failed", 
            "message": "Login failed"+ email
        }
        return jsonify(response), 401

@bp.route('/register', methods=["POST"])
def register():
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email, password=password).first()

    if user is not None:
        response = {
            "status": "failed",
            "message": "already users: " + email
        }
        return jsonify(response), 401
    else: 
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

    return jsonify({"status": "success", "message": "Register Success"})
```

上記の例では、`@bp.route`を使用してルーティングを定義し、それぞれの関数に対してHTTPメソッドを指定しています。また、ユーザーやメッセージに関するデータベース操作は、各モデルを介して行っています。

これらのビューは、`application/views/__init__.py`で作成したBlueprintによりFlaskアプリケーションに登録されます。このBlueprintは、`application/__init__.py`でインポートし、Flaskアプリケーションの作成時に登録します。

最後に、`application/__init__.py`でアプリケーションを初期化する際に、`application/views/__init__.py`からBlueprintをインポートし、Flaskアプリケーションに登録します。