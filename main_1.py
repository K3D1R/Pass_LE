# password manager

"""
available commands:
/add
/get_pass
/info
/all_logins
"""

import access
from getpass import getpass


print('initialising.....')

print('=================PASS_LE=================')
available = True
while available:
    usr_command = input()
    if usr_command == '/info':
        print("""
        Список доступных команд:
        /add,
        /get_pass,
        /info,
        /all_logins
        """)

    elif usr_command == '/add':
        url = input("URL>>> ")
        login=input('Введите логин>>> ')
        password=getpass('Введите пароль>>> ')
        access.make_account(url, password, login)
        print('Учётная запись успешно добавлена!')

    elif usr_command == '/get_pass':
        login = input("Введите Логин учётной записи. Внимание, важен каждый символ. ")
        password = access.get_pass(login)

    elif usr_command == '/all_logins':
        for login in access.get_logins():
            print(login[0])
    
    elif usr_command == '/delete':
        sure=input("Вы ТОЧНО уверены в том, что хотите ___БЕЗВОЗРАТНО___ удалить данные? ")
        if sure.upper()=='ДА':
            url = input()
            login=input()
            password=input()
        
            access.delete_data(url ,login, password)
            print('Success')
        else:
            print('ok')
    elif usr_command == '/exit':
        available=False
    
    else:
        print("Unavailable command")

else:
    access.close()
