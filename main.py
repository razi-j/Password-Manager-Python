from functions import Pwman
import getpass

if __name__ == "__main__":
    while True:
        print("Hidden Keys")

        ch = input("""What do you want to do?
        1. Generate A Key
        2. Add Password
        3. View Passwords
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