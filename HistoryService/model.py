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

class History:
    def __init__(self):
        self.login_model = """
                            CREATE TABLE IF NOT EXISTS history (
                                id integer PRIMARY KEY,
                                username text,
                                history text
                            );
                            """
        sql_command(self.login_model)
    
    def get_history(self, username):
        query_history_cmd = """
                            SELECT * from history WHERE username = '{}'
                            """.format(username)

        results = sql_command(query_history_cmd)
        return results
    
    def add_history(self, username, date, story):
        query_history_cmd = """
                            SELECT * from history WHERE username = '{}'
                            """.format(username)
        
        results = sql_command(query_history_cmd)
        history = json.loads(results['data']['history'])

        if date in history:
            return 

        history[date] = story
        history_str = json.dumps(history)

        update_history_cmd = """
                            UPDATE history
                            SET history = '{}'
                            WHERE username = '{}'
                            """.format(history_str, username)
    
    def check_history(self, username, date):
        query_history_cmd = """
                            SELECT * from history WHERE username = '{}'
                            """.format(username)
        
        results = sql_command(query_history_cmd)
        history = json.loads(results['data']['history'])

        if date in history:
            return True

        return False
    
    