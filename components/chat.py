from flask import Flask, render_template, request, Blueprint, session, jsonify
import datetime
from database import get_db 


chat = Blueprint('chat', __name__)

messages = []

@chat.route('/chat', methods=['POST'])
def post_message():
    user_id = session.get('user_id')
    message = request.json['message']
    
    timestamp = datetime.datetime.now().isoformat()
    messages.append({'message': message, 'user_id': user_id})
    con = get_db()
    cur = con.cursor()
    cur.execute("INSERT INTO MESSAGES (MESSAGE, USER_ID) VALUES (? , ?)", (message, user_id))
    con.commit()

    return jsonify(success=True)

@chat.route('/chat', methods=['GET'])
def chat_page():
    return render_template('chatlist.html')

@chat.route('/get_messages', methods=['GET'])
def get_messages():
    user_id = session.get('user_id')
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM MESSAGES WHERE USER_ID = ? ORDER BY CREATED_AT ASC", (user_id,))
    userMessages = cur.fetchall()
    cur.execute("SELECT * FROM MESSAGES ORDER BY CREATED_AT ASC")
    allMessages = cur.fetchall()

    userMessageList = [dict(row) for row in userMessages]
    allMessagesList = [dict(row) for row in allMessages]
    return jsonify(userMessageList=userMessageList, allMessagesList=allMessagesList)