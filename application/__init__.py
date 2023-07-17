import os
from flask import Flask, render_template
from .routes.chat import chat
from .routes.login import auth
import secrets

def generate_secret_key():
    return secrets.token_hex(16)

def create_app():
    app = Flask(__name__, static_folder=os.path.join(os.pardir, 'static'))
    app.secret_key =  generate_secret_key()
    app.register_blueprint(chat)
    app.register_blueprint(auth)

    @app.route('/')
    def home():
        return render_template('index.html')

    return app