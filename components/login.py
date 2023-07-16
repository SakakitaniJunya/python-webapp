from flask import Blueprint, render_template, request, jsonify
import sqlite3
import tkinter

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")


    # con = sqlite3.connect('chat.db')
    # cur = con.cursor()
    # cur.execute("SELECT * FROM USERS WHERE email = ? AND password = ?", (email, password))
    
        # メッセージをレスポンスとして返す
    response = {
        "status": "success", 
        "message": "Login successful."+ password
    }

    return jsonify(response)


# @auth.route('/login', methods=["GET"])
# def login():
#     email = request.form.get("email")
#     password = request.form.get("password")

#     print(email)
#     print(password)

#     # con = sqlite3.connect('chat.db')
#     # cur = con.cursor()
#     # cur.execute("SELECT * FROM USERS WHERE email = ? AND password = ?", (email, password))
#     # tkinterのインポート
#     return "Hello"

