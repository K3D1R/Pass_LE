# password manager

"""
available commands:
/add
/get_pass
/info
/all_logins
"""
print('initialising.....')



from password import pass_dict
from getpass import getpass


print('==================================PASSLE==================================')
print("""
Приветствуем Вас в программе PassLE! Для того чтобы ознакомиться со списком доступных для использования команд введите команду /info
""")

while True:
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
        login=input('Введите логин>>> ')
        password=getpass('Введите пароль>>> ')
        pass_dict[login]=password
        print('Учётная запись успешно добавлена!')

    elif usr_command == '/get_pass':
        login = input("Введите Логин учётной записи. Внимание, важен каждый символ. ")
        print(f"Пароль от учётной записи {login}>>> {pass_dict[login]}")

    elif usr_command == '/all_logins':
        for login in pass_dict.keys():
            print(login)
