import password_generator as pg
from password_manager import Password_manager
from secret import SECRET_PASSWORD, DB_PASSWORD
import sys
import os
from time import sleep
from getpass import getpass
def menu():
 
    pm = Password_manager()

    password = getpass('Enter secret key: ')
    if password != SECRET_PASSWORD:
        print('Sorry, password incorrect')
        sys.exit()

    else:
        print('         Welcome Szymon!')
        sleep(2)
        os.system('clear')
    
    
    while True:
        print('\n'*2)
        print('#'*10+'MENU'+'#'*10)
        print('1.Add existing account.')
        print('2.Generate password for account.')
        print("3.Change account's passowrd.")
        print("4.Find password for account.")
        print("5.Find all accounts connceted to email.")
        print("6.Delete account from database.")
        print("0.Exit")


        choose_option(pm)






def choose_option(pm):

    command = int(input('Select options 0 to 6: '))
    sleep(1)
    os.system('clear')
     
    if command == 1:
        pm.store_existing_account()
    elif command == 2:
        pm.generate_password()
    elif command == 3:
        pm.change_password()
    elif command == 4:
        pm.find_password()
    elif command == 5:
        pm.find_accounts()
    elif command == 6:
        pm.delete_account()
    elif command == 0:
        print("Bye")
        sys.exit()










if __name__ == "__main__":
    menu()
