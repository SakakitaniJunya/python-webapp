from flask import Flask, render_template, request, Blueprint
import sqlite3

chat = Blueprint('chat', __name__)


@chat.route('/chat', methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM USERS WHERE email = ? AND password = ?", (email, password))
    user = cur.fetchone()

    if user is not None:
        response = {
            "status": "success",
            "message": "user"
        }