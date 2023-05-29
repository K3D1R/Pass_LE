# password manager

"""
available commands:
/add
/get_pass
/info
/all_logins
/delete
"""
#импорт нужных библиотек

import access
from art import tprint
from simple_term_menu import TerminalMenu
from getpass import getpass


def choose_login():
    """
    Оформление получение логина с помощью меню в консоли
    """
    try:
        len(access.get_logins())
        print('Выберите логин:')
        logins = list()
        for login in access.get_logins():
            logins.append(login[0])
        terminal_menu = TerminalMenu(logins)
        menu_index=terminal_menu.show()
        login = logins[menu_index]   
        return login
    except:
        return False 

commands=['/add', '/get_pass', '/info', '/all_logins', '/delete', '/exit']





print('initialising.....')
tprint('Pass_LE')
available = True
print("""
        Список доступных команд:
        /add - добавить учётную запись
        *необходимо иметь ссылку сайта, логин, пароль,
        /get_pass - получить пароль от учётной записи
        *необходимо иметь логин необходимой учётной записи,
        /info,
        /all_logins - просмотр всех логинов(уч. записей),
        /delete - удаление конкретной учётной записи
        *необходимо иметь ссылку, логин, пароли учётной записи
        /exit - выход из программы
        """)

status = False

def is_usr_log_empty():
    global status
    if access.get_usr_logs() == 0:
        print("Создайте учётную запись PassLE")
        usr_log = input('Введите логин>> ')
        password = input('Введите Мастер-пароль. Внимание! Мастер-пароль нельзя восстановить. В случае его утери доступ получить невозможно>> ')
        data = [usr_log, password, 0]
        status = access.regist(data)
    else:
        usr_log = input("Введите логин PassLE>> ")
        password = getpass("Введите пароль PassLE>> ")
        data = [usr_log, password, 1]
        status = access.regist(data)
 
    
    
#Основной цикл программы
while available:
    is_usr_log_empty()
    if status == True:
        cms=TerminalMenu(commands)
        cms_index=cms.show()
        usr_command = commands[cms_index]
        if usr_command == '/info':
            print("""
            Список доступных команд:
            /add - добавить учётную запись
            *необходимо иметь ссылку сайта, логин, пароль,
            /get_pass - получить пароль от учётной записи
            *необходимо иметь логин необходимой учётной записи,
            /info,
            /all_logins - просмотр всех логинов(уч. записей),
            /delete - удаление конкретной учётной записи
            *необходимо иметь ссылку, логин, пароли учётной записи
            """)

        elif usr_command == '/add':
            url = input("URL>>> ")
            login=input('Введите логин>>> ')
            password=getpass('Введите пароль>>> ')
            access.make_account(url, password, login)
            print('Учётная запись успешно добавлена!\n')

        elif usr_command == '/get_pass':
            
            password = access.get_pass(choose_login())
            
        
        elif usr_command == '/all_logins':
            for login in access.get_logins():
                print(login[0])
        
        elif usr_command == '/delete':
            sure=input("Вы ТОЧНО уверены в том, что хотите ___БЕЗВОЗРАТНО___ удалить данные? ")
            if sure.upper()=='ДА':
                
                access.delete_data(choose_login())
            else:
                print('ok')
        elif usr_command == '/exit':
            available=False
        
        else:
            print("Unavailable command")
    else:
        pass

else:
    tprint('GOODBYE')
    access.close()
