"""
In this file you will see all methods, which descript main functions of this programm.
You can also look through access.py to get known about work with DB with helf of DB class
"""


import getpass
from ciph import aesenc, aesdec, encrypts
from access import db
from tabulate import tabulate
#--------------------------------------------------
current_user_id = None
reg=None
active = True
#--------------------------------------------------

def available_user(function_0):
    """
    This decorator takes function and before doing it checks if user has logged in his PassLE account
    :param function_0:
    :return:
    """
    def wrapper():
        if current_user_id:
            function_0()
            return function_0
        else:
            print("Вы не вошли в аккаунт")
    return wrapper

def get_in(login, password):
    password = encrypts(password)
    value = db.get_in(login, password)
    global current_user_id
    if isinstance(value, tuple):
        current_user_id = value[1]
        #print(current_user_id)

def log_in():
    """
    It takes from user login and password and, usin DB.get_in() compare with db
    You should look through the description of the DB.get_in()
    :return:
    """
    login = input('Login>>> ')
    password = input('Password>>> ')

    get_in(login, password)

def registration():
    """
    It takes no args.
    This function asks login from user and password with two inputs and put this data into the dictionary
    with key login (for login) and password (for password)
    :return:
    """
    print("""
    \nRegistration\nMenu\n
""")
    login = input('Login>>> ')
    print(login)
    password = getpass.getpass('Password>>> ')
    sc_password = getpass.getpass('input password another time>>')
    if password == sc_password:
        db.registr(login, encrypts(password))
        get_in(login, password)
        reg=1
        #print(current_user_id)
    else:
        print("Input password aren't aren't same. Try again")
        registration()

@available_user
def get_record():
    url = input('Url>>> ')
    login = input('Login>>> ')
    password = db.get_record(current_user_id, url, login)
    print(f'Password>>> {aesdec(password,current_user_id)}')


@available_user
def get_all_records():
    records_list = db.get_all_users_records(current_user_id)

    if len(records_list)>0:
        res = {'URL':[], 'Login':[]} 
        for number, record in enumerate(records_list):
            url, login = record
            res['URL'].append(url)
            res['Login'].append(login)
            #print(f'Url {number+1}>>> {url}')
            #print(f'Login {number+1}>>> {login}')
        print(tabulate(res, headers='keys'))
    else:
        print("Отсутствуют записи!\n")

@available_user
def new_record():
    """
    This function
    :return:
    """
    url = input('Url>>> ')
    login = input('Login>>> ')
    password = aesenc(input('Password>>> '), current_user_id)
    db.add_record(current_user_id, url, login, password)

@available_user
def delete_record():
    """
    this function delete record in the records table using user_id, login, url
    :return:
    """
    url = input('Url>>> ')
    login = input('Login>>> ')
    db.delete_record(current_user_id, url, login)

@available_user
def edit_record():
    url = input('Url>>> ')
    login = input('Login>>> ')
    if db.get_record(current_user_id, url, login):
        record_id = db.get_record_id(current_user_id, url, login)
        choose_list = ['Url', 'Login', 'Password']
        choose = input('Url, Login, Password ?')
        if choose in choose_list:
            if choose == 'Url':
                new_url = input('Input new_url>>> ')
                db.edit_record(choose, new_url, record_id)
            elif choose == 'Login':
                new_login = input('Input new_login>>> ')
                db.edit_record(choose, new_login, record_id)
            elif choose == 'Password':
                new_password = input('Input new_password>>> ')
                db.edit_record(choose, aesenc(new_password, current_user_id), record_id)
        else:
            print("Введён неверный тип")
    else:
        print('Учётной записи с такими данными не существует')


@available_user
def utflen():
  print(db.get_pass(current_user_id).encode('utf-8'))
  print(len(db.get_pass(current_user_id).encode('utf-8')))

def exit():
    global active 
    active = False

def action():

    if isinstance(current_user_id, int) or reg:
      print("""
                !FAQ!\n
             1 - get_record;\n
            2 - get_all_records;\n
            3 - new_record; \n
            4 - delete_record; \n
            5 - edit_record;\n
            6 - exit\n
            """
            )
      choose = int(input("Выберите действие>> "))
      match choose:
                case 1:
                    get_record()
                case 2:
                    get_all_records()
                case 3:
                    new_record()
                case 4:
                    delete_record()
                case 5:
                    edit_record()
                case 6:
                    exit()
                case 7:
                    utflen()
                case _:
                    print("Wrong command!")

    else:
      own_account = input("Do you have an account? y/n\n")
      match own_account.lower():
          case 'y':
              log_in()
          case 'n':
              registration()
          case _:
              print("Wrong answer!")


def main():
    while active:
        action()


if __name__ == '__main__':
    main()