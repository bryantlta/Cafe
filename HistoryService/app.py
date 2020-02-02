from flask import Flask, jsonify, request

from model import History

app = Flask(__name__)

history_model = History()

@app.route('/history', methods=['GET', 'POST'])
def history():
    if request.method == 'GET':
        user_data = request.get_json()
        username = user_data['username']
        history_model.get_history(username)
    
    elif request.method == 'POST':
        user_data = request.get_json()
        username = user_data['username']
        date = user_data['date']
        history = user_data['history']
        history_model.add_history(username, date, history)


@app.route('/historycheck', methods=['POST'])
def historycheck():
    user_data = request.get_json()
    username = user_data['username']
    date = user_data['date']
    check = history_model.check_history(username)

    if check:
        return True
    
    return False
