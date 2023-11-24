"""
In this file you can see all methods, what programm's going to use to access to DB.
Each of this methods is part of special class 'DB'. I will try to left comments near
to each method.
"""


import sqlite3
conn = sqlite3.connect("password.db")
cursor = conn.cursor()

class DB:
    def __init__(self):
        """
        Here we make two tables:
        /*user*/, where we store accounts of user in our programm
        records,  where user store his/her accounts of other sites, programms, etc.
        """
        query = """
        CREATE TABLE IF NOT EXISTS 'users' (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
            name TEXT ,
            password TEXT
        );
        CREATE TABLE IF NOT EXISTS 'records' (
                    record_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
                    user_id INT ,
                    url TEXT ,
                    name TEXT ,
                    password TEXT
        )
        """
        cursor.executescript(query)
        conn.commit()
        print('Подключение к базе данных выполнено!')

    def registr(self, login: str, password: str):
        """
        It takes two args login and password and fill with them table users in the db
        :param login:
        :param password:
        :return:
        """
        if not cursor.execute("""SELECT EXISTS (SELECT * FROM users WHERE name = (?))""", (login,)).fetchone()[0]:
          cursor.execute("INSERT INTO users(name, password) VALUES (?, ?)", (login, password))
          conn.commit()
        else:
          print("Такая учётная запись уже существует")

    def get_in(self, login: str, password: str):
        """
        This function get login and password from args and from database and compare them. If they're the same
        it should return True in the var pass_ac. Else it will get you value False
        :param login:
        :param password:
        :return: pass_ac
        """
        find = 0
        logins_from_db = cursor.execute("""
        SELECT name FROM users
        """).fetchall()
        #print(logins_from_db)

        for login_o in logins_from_db:
            login_o=login_o[0]
            print(login_o)

            if login_o == login:
                find = 1
                break
            else:
                continue
        if find == 1:

            password_o = cursor.execute("""SELECT password FROM users WHERE name = (?)""", (login,)).fetchone()[0]
            #print(password_o)

            if password_o == password:
                user_id = cursor.execute("""SELECT user_id FROM users WHERE name = (?)""", (login,)).fetchone()[0]
                #print(user_id)
                return 1, user_id

            else:
                return 10

        else:
            return 0

    def add_record(self, user_id: int, url: str, record_login: str, password: str):
        """
        This function add new record to record table to the current user
        :param user_id:
        :param url:
        :param login:
        :param password:
        :return:
        """
        if not cursor.execute("""SELECT EXISTS (SELECT * FROM records WHERE user_id = (?) AND url = (?) AND name = (?))""", (user_id, url, record_login)).fetchone()[0]:
          cursor.execute("""
          INSERT INTO records(user_id, url, name, password) VALUES (?, ?, ?, ?)""", (user_id, url, record_login, password))
          conn.commit()
          print("Успешно!")
        else:
            print("Такая запись уже существует!")

    def get_record(self, user_id: int, url: str, record_login: str):
        #This function asks these arguments and look through the table record
        password = cursor.execute("""SELECT password FROM records WHERE user_id = (?) AND url = (?) AND name = (?) """, (user_id, url, record_login)).fetchone()[0]
        return password

    def get_record_id(self, user_id: int, url: str, record_login: str):
        # This function asks these arguments and look through the table record
        return cursor.execute("""SELECT record_id FROM records WHERE user_id = (?) AND url = (?) AND name = (?) """,
                              (user_id, url, record_login)).fetchone()[0]

    def get_all_users_records(self, user_id: int):
        return cursor.execute("""SELECT url, name FROM records WHERE user_id = (?)""", (user_id,)).fetchall()

    def delete_record(self, user_id: int, url: str, record_login: str):
        if cursor.execute("""SELECT EXISTS (SELECT * FROM records WHERE user_id = (?) AND url = (?) AND name = (?))""", (user_id, url, record_login)):
            cursor.execute("DELETE FROM records WHERE user_id = (?) AND url = (?) AND name = (?)", (user_id, url, record_login))
            conn.commit()

    def edit_record(self, type_of_changing: str, new_data: str, record_id: int):
        """

        :param type_of_changing: Url/Login/Password
        :param new_data:
        :param record_id: unique number of each recording
        :return:
        """
        if type_of_changing == 'Url':
            cursor.execute("""UPDATE records SET url = (?) WHERE record_id = (?)""", (new_data, record_id))
        elif type_of_changing == 'Login':
            cursor.execute("""UPDATE records SET name = (?) WHERE record_id = (?)""", (new_data, record_id))
        elif type_of_changing == 'Password':
            cursor.execute("""UPDATE records SET password = (?) WHERE record_id = (?)""", (new_data, record_id))
        conn.commit()

    def all_users_records(self):
        """
        It prints you all record in table users
        :return:
        """
        data = cursor.execute("SELECT * FROM users").fetchall()

    def get_pass(self, user_id:int):
        #print(type(user_id))
        passw = cursor.execute("SELECT password FROM users WHERE user_id = (?)", (user_id,)).fetchone()[0]
        return passw


    def close(self):
        conn.close()

db = DB()


