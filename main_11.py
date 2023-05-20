# password manager

"""
available commands:
/add
/get_pass
/info
/all_logins
/delete
"""

import access
from art import tprint
from simple_term_menu import TerminalMenu
from getpass import getpass


print('initialising.....')

tprint('PASS_LE')
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
while available:
    usr_command = input()
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
        print('Учётная запись успешно добавлена!')

    elif usr_command == '/get_pass':
        
        len(access.get_logins())
        print('Выберите логин:')
        logins = list()
        for login in access.get_logins():
            logins.append(login[0])
        terminal_menu = TerminalMenu(logins)
        menu_index=terminal_menu.show()
        login = logins[menu_index]
        password = access.get_pass(login)
        
       
    elif usr_command == '/all_logins':
        for login in access.get_logins():
            print(login[0])
    
    elif usr_command == '/delete':
        sure=input("Вы ТОЧНО уверены в том, что хотите ___БЕЗВОЗРАТНО___ удалить данные? ")
        if sure.upper()=='ДА':
            url = input('Введите ссылку учётной записи к удалению>>> ')
            login=input('Введите логин учётной записи к удалению>>> ')
            password=input('Введите пароль учётной записи к удалению>>> ')
        
            access.delete_data(url ,login, password)
            print('Успешно!')
        else:
            print('ok')
    elif usr_command == '/exit':
        available=False
    
    else:
        print("Unavailable command")

else:
    access.close()
