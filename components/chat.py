from flask import Flask, render_template, request, Blueprint
import sqlite3

chat = Blueprint('chat', __name__)


@chat.route('/chat', methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    con = sqlite3.connect('chat.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM USERS WHERE email = ? AND password = ?", (email, password))