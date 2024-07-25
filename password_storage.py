from time import sleep


def permission(accounts, passwords, name): # function with the ability to enter multiple accounts
    PASSWORDS = dict(zip(accounts, passwords))
    print(f'Hello, {name}!')
    while True:
        account = input("Enter your account name").lower()
        print(PASSWORDS.get(account, "Account does not exist"))
        is_continue = input("Do you want continue? (Y/N): ")
        if is_continue.upper() == "Y":
            continue
        else:
            print(f'Good bye, {name}!')
            sleep(0.6)
            break


account_passwords = {'password0': ('file0.csv', 'Arthur'), 'password1': ('file1.csv', 'user_name1'),
                     'password2': ('file2.csv', 'user_name2'), 'password3': ('file3.csv', 'user_name3')} # variable, to get file.csv(excel table.csv) and user name from password
file_password = input('Enter your access code: ')
user = account_passwords.get(file_password, 'not found')
if file_password in account_passwords:
    with open(f'path/{account_passwords[file_password][0]}', encoding='UTF-8') as file:
        acc = list(map(lambda word: word.lower(), file.readline().rstrip().split(';')))
        pasw = file.readline().strip().split(';')
        permission(accounts=acc, passwords=pasw, name=user[1])

else:
    print("Password does not exist")

sleep(0.5)
