from time import sleep


def permission(accounts, passwords, name): # function with the ability to enter multiple accounts
    PASSWORDS = dict(zip(accounts, passwords))
    print(f'Здравствуйте, {name}!')
    while True:
        account = input("Введите учетную запись: ").lower()
        print(PASSWORDS.get(account, "Учетная запись не найдена"))
        is_continue = input("Хотите продолжить? (Y/N): ")
        if is_continue.upper() == "Y":
            continue
        else:
            print('До свидания')
            sleep(0.6)
            break


account_passwords = {'password0': ('file0.csv', 'user_name0'), 'password1': ('file1.csv', 'user_name1'),
                     'password2': ('file2.csv', 'user_name2'), 'password3': ('file3.csv', 'user_name3')} # variable, to get file.csv(excel table.csv) and user name from password
file_name = input('Введите код доступа: ')
user = account_passwords[file_name][1]
if file_name in account_passwords:
    with open(f'path/{account_passwords[file_name][0]}') as file:
        acc = file.readline().strip().split(';')
        pasw = file.readline().strip().split(';')
        permission(accounts=acc, passwords=pasw, name=user)

else:
    print("Пароль не найден")

sleep(0.5)
