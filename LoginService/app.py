from flask import Flask, jsonify, request

from model import Login

app = Flask(__name__)

login_model = Login()

@app.route('/login', methods=['POST'])
def login():
    login_data = request.get_json()
    username = login_data['username']
    password = login_data['password']
    check = login_model.login(username, password)

    if check:
        return "You have successfully logged in!"
    
    return "Failed to log in!"

@app.route('/signup', methods=['POST'])
def signup():
    signup_data = request.get_json()
    username = login_data['username']
    password = login_data['password']
    check = login_model.signup(username, password)

    if check:
        return "You have successfully signed up!"
    
    return "Failed to sign up!"