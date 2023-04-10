from functions import Pwman
import getpass
import os

if __name__ == "__main__":
    while True:
        if os.name =="nt":
                os.system("cls")
        elif os.name =="posix":
                os.system("clear")
        
        ch = input("""
            Hidden Keys
        What do you want to do?
        1. Generate A Key
        2. Add Password
        3. View Passwords
        q. Quit
""")
        if ch == "1":
            password = getpass.getpass("Set a Master Password: ")
            Pwman.buildKey(password)
        elif ch == "2":
            key = Pwman.loadKey()
            encrypt = Pwman.auth(key)
            Pwman.addPassword(encrypt)

        elif ch == "3":
            key = Pwman.loadKey()
            encrypt = Pwman.auth(key)
            Pwman.view(encrypt)
        
        elif ch == "q":
            print("Goodbye!")
            if os.name =="nt":
                os.system("cls")
            elif os.name =="posix":
                os.system("clear")
            quit()