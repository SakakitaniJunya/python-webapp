from flask import Blueprint, render_template, request
import sqlite3

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    con = sqlite3.connect('chat.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM USERS WHERE email = ? AND password = ?", (email, password))