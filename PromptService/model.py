import sqlite3
from sqlite3 import Error

import json

def sql_command(command):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        result = cursor.execute(command)
        result = result.fetchall()
        conn.commit()

        cursor.close()
    except Error as e:
        return e
    
    return result

class Reinforcement_Learning:
    def __init__(self):
        self.login_model = """
                            CREATE TABLE IF NOT EXISTS rl (
                                id integer PRIMARY KEY,
                                username text,
                                state text,
                            );
                            """
        sql_command(self.login_model)

    def initialize_user(self, username):
        if self.check_user(username):
            return 

        state = {}
        for i in range(1, 31):
            state[i] = 0

        state = json.dumps(state)

        initialize_cmd = """
                        INSERT INTO rl
                        (id, username, state)
                        VALUES
                        (NULL, '{}', '{}')
                        """.format(username, state)
        
        sql_command(initialize_cmd)
    
    def check_user(self, username):
        query_cmd = """
                    SELECT * FROM rl WHERE username = '{}'
                    """.format(username)
        
        result = sql_command(query_cmd)
        if result:
            return True
        
        return False

    def get_state(self, username):
        if !self.check_user(username):
            return 

        query_cmd = """
                    SELECT * FROM rl WHERE username = '{}'
                    """.format(username)
        
        result = sql_command(query_cmd)
        return result
    
    def update_states(self, username, chapter, new_time):
        if !self.check_user(username):
            return 
        
        query_cmd = """
                    SELECT * FROM rl WHERE username = '{}'
                    """.format(username)
        
        result = sql_command(query_cmd)
        state = result['data']['state']
        jsonified_state = json.loads(state)
        jsonified_state[chapter] = new_time
        state = json.dumps(jsonified_state)
        
        update_cmd = """
                    UPDATE rl
                    SET state = '{}'
                    WHERE username = '{}'
                    """.format(state, username)

        sql_command(update_cmd)