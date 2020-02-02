from flask import Flask, jsonify, request

from model import Reinforcement_Learning

import json

app = Flask(__name__)

rl_model = Reinforcement_Learning()
epsilon = 0.4
learning_rate = 0.5

@app.route('/prompt', methods=['GET', 'POST'])
def new_prompt():
    if request.method == 'GET':
        data = request.get_json()
        username = data['username']

        chapter = get_prompt(username, epsilon)
        return chapter

    elif request.method == 'POST':
        data = request.get_json()
        username = data['username']
        chapter = data['chapter']
        time = data['time']
        update_state(username, chapter, time, learning_rate)


def get_prompt(username, epsilon):
    # Epsilon is for epsilon-greedy policy

    if !rl_model.check_user(username):
        rl_model.initialize_user(username)
    
    states = rl_model.get_state(username)['data']
    jsonStates = json.loads(states)
    
    max_state = 0
    max_time = 0
    for i in range(1, 31):
        if jsonStates[i] >= max_time:
            max_state = i
            max_time = jsonStates[i]
    
    random_value = Math.random()

    if random_value < epsilon:
        return max_state

    else:
        increment = 1/29
        random_value = Math.random()
        curr_value = 0
        i = 1

        while curr_value < random_value:
            if i != max_state:
                curr_value += increment
            
            i += 1
        return i

def update_state(username, chapter, new_time, learning_rate):
    # Temporal Difference Learning 

    if !rl_model.check_user(username):
        rl_model.initialize_user(username)

    states = rl_model.get_state(username)['data']
    jsonStates = json.loads(states)

    curr_time = jsonStates[chapter]
    time = (1 - learning_rate) * curr_time + learning_rate * new_time
    rl_model.update_states(username, chapter, time)
