
from flask import Blueprint, render_template, request, jsonify, session
import sqlite3
from database import get_db 

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    con =get_db() 
    cur = con.cursor()
    cur.execute("SELECT * FROM USERS WHERE email = ? AND password = ?", (email, password))
    user = cur.fetchone()
        # メッセージをレスポンスとして返す
    if user is not None:
        # セッションに格納
        session['user_id'] = user['user_id']
        session['email'] = user['email']
        session['user_name'] = user['name']
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



@auth.route('/register', methods=["POST"])
def register():
    email = request.form.get("email")
    password = request.form.get("password")

    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM USERS WHERE email = ? AND password = ?", (email, password))
    user = cur.fetchone()
    ## ユーザがすでに存在しているかどうかを確認
    if user is not None:
        response = {
            "status": "failed",
            "message": "already users: " + email
        }
        return jsonify(response), 401
    else: 
        cur.execute("INSERT INTO USERS (EMAIL, PASSWORD) VALUES (? , ?)", (email, password))
        con.commit()

    return jsonify({"status": "success", "message": "Register Success"})