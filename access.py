import sqlite3
conn = sqlite3.connect("password.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS accounts(url TEXT, login TEXT, password TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS usr_log(login TEXT, password TEXT)")
conn.commit()

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

def make_account(url,password,login):
    cursor.execute("INSERT INTO accounts VALUES (?,?,?)", (url, login, password),)
    conn.commit()

def get_logins():
    logins = cursor.execute("SELECT login FROM accounts")
    logins=logins.fetchall()
    return logins

def get_pass(login):
    try:
        password = cursor.execute("SELECT password FROM accounts WHERE login=(?)", (login,))
        print(f'Пароль от учётной записи {login}>>> {password.fetchone()[0]}')
    except:
        print('Ошибка')

def delete_data(url,login,password):
    cursor.execute("DELETE FROM accounts WHERE url = ?",(url,))
    conn.commit()

def close():
    conn.close()