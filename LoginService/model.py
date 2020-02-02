import sqlite3
from sqlite3 import Error

from werkzurg.security import generate_password_hash, check_password_hash

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

class Login:
    def __init__(self):
        self.login_model = """
                            CREATE TABLE IF NOT EXISTS login (
                                id integer PRIMARY KEY,
                                username text,
                                password text,

                            );
                            """
        sql_command(self.login_model)

    def signup(self, username, password):

        check_username_cmd = """
                        SELECT * FROM login WHERE username='{}'
                        """.format(username)
        
        result = sql_command(check_username_cmd)
        if (result):
            return False

        password = generate_password_hash(password)

        signup_command = """
                        INSERT INTO login
                        (id, username, password)
                        VALUES
                        (NULL, '{}', '{}')
                        """.format(username, password)

        sql_command(signup_command)
        return True
    
    def login(self, username, password):
        query_user_command = """
                            SELECT * FROM login WHERE username='{}'
                            """.format(username)
        
        query_result = sql_command(query_user_command)

        db_password = query_result['data']['password']
        
        password_check = check_password_hash(password, db_password)

        if password_check:
            return True
        
        return False
        

    
    