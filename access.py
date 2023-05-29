import sqlite3
conn = sqlite3.connect("password.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS accounts(url TEXT, login TEXT, password TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS usr_log(login TEXT, password TEXT)")
conn.commit()


"""##test_features
def create_passle_id(code):
    try:
        len(cursor.execute("SELECT login FROM usr_log ").fetchone()[0])
    except:
        count = 0
    if count==0:
        login = input()
        password = input()
        cursor.execute("INSERT INTO usr_log account VALUES (?, ?)", (login, password,))
        conn.commit()
        print('Успешно!')
    
    elif count == 0 and code==1:
        print('У Вас уже имеется учётная запись PASS_LE')

    else:
        code = 1   

def sign_in(login, password):
    pass_id_login = cursor.execute('SELECT login FROM usr_log').fetchone()[0]
    pass__id_password = cursor.execute('SELECT password FROM usr_log').fetchone()[0]
    if pass_id_login == login:
        if pass__id_password == password:
            return True
        else:
            return False
    else:
        return False
"""
#production



def regist(data):
    if type(data) is list:
        if data[2] == 0:
            login = data[0]
            password = data[1]
            cursor.execute('INSERT INTO usr_log VALUES (?,?)', (login, password),)
            conn.commit()
        if data[2] == 1:
            t_pass = cursor.execute('SELECT password FROM usr_log').fetchone()[0]
            t_log = cursor.execute('SELECT login FROM usr_log').fetchone()[0]
            password = data[1]
            login = data[0]
            if t_pass == password and t_log == login:
                return True
            else:
                return False
    else:
        raise TypeError
   

def get_usr_logs():
    login = cursor.execute("SELECT login FROM usr_log")
    login = login.fetchall()
    login = len(login)
    return login

def make_account(url,password,login):
    """
    Создание зиписи пароля, логина, ссылки
    """
    cursor.execute("INSERT INTO accounts VALUES (?,?,?)", (url, login, password),)
    conn.commit()

def get_logins():
    """
    Получение списка логинов
    """
    logins = cursor.execute("SELECT login FROM accounts")
    logins=logins.fetchall()
    return logins

def get_pass(login):
    """
    Получение пароля пользователя по логину
    """
    try:
        password = cursor.execute("SELECT password FROM accounts WHERE login=(?)", (login,)).fetchone()[0]
        url = cursor.execute("SELECT url FROM accounts WHERE login=(?)", (login,)).fetchone()[0]
        print(f'Пароль от учётной записи {login}>>> {password}\nСсылка на сайт уч. записи>>> {url}')
    except:
        print('Ошибка')

def delete_data(login):
    """
    Удаление данных об учётной записи по логину
    """
    if login == False:
        print("Отсутствуют учётные записи!\n")

    else:
        url = cursor.execute("SELECT url FROM accounts WHERE login = ?", (login,)).fetchone()[0]
        cursor.execute("DELETE FROM accounts WHERE url = ?",(url,))
        conn.commit()
        print("Успешно!\n")

def close():
    conn.close()