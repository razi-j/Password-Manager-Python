from functions import Pwman
import getpass

if __name__ == "__main__":
    while True:
        print("\t\tHidden Keys")
        ch = input("""What do you want to do?
        1. Generate A Key
        2. View Passwords
        3. Add Passwords
        """)
        if ch == "1":
            password = getpass.getpass("Set a Master Password: ")
            Pwman.buildkey(password)