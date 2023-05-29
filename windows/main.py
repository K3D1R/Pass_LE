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

from getpass import getpass

def choose_login():
    """
    Оформление получение логина с помощью меню в консоли
    """
    logins = access.get_logins()
    for login in logins:
        print(login[0])
    login = input("Введите логин:")
    if login in logins:
        return login
    else:
        return 'error'


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
    #cms=TerminalMenu(commands)
    #cms_index=cms.show()
    #usr_command = commands[cms_index]
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
        print('Учётная запись успешно добавлена!\n')

    elif usr_command == '/get_pass':
        
        try:
            access.delete_data(choose_login())
        except:
            print('\n')
       
    elif usr_command == '/all_logins':
        for login in access.get_logins():
            print(login[0])
    
    elif usr_command == '/delete':
        sure=input("Вы ТОЧНО уверены в том, что хотите ___БЕЗВОЗРАТНО___ удалить данные? ")
        if sure.upper()=='ДА':
            try:
                access.delete_data(choose_login())
            except:
                print('\n')
        else:
            print('ok')
    elif usr_command == '/exit':
        available=False
    
    else:
        print("Unavailable command")

else:
    tprint('GOODBYE')
    access.close()
