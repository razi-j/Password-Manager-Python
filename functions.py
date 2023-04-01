import base64
import os
import getpass
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC # Password Based Key Derive Function
from cryptography.fernet import Fernet
import time

class Pwman:
    @classmethod
    def keygen(cls,pw):
        password = pw.encode()
        with open("salt", "rb") as saltf:
            salt = bytes(saltf.read())
        kdf = PBKDF2HMAC(
                    algorithm=hashes.SHA256,
                    salt=salt,
                    length=32,
                    iterations=480000
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        with open("./key", "wb") as keyf:
            keyf.write(key)
        return key

    @classmethod
    def buildKey(cls, pw):
        if os.path.exists("./key"):
            ch = input("Key Already Exists!\nGenerate a new key?(y/n) ")
            if ch.lower() != "y" and ch.lower() != "n":
                print("Invalid Input")
            else:
                if ch.lower()=="y":
                    if os.path.exists("./salt") == False:
                        cls.genSalt()
                        print("Salt Generated")
                    else:
                        choice = input("Rebuild Salt?(y/n) ")
                        if choice == "y":
                            cls.genSalt()
                            print("Salt Generated")
                        elif choice == "n":
                            pass
                        else:
                            print("Invalid Input")
                    cls.keygen(pw)
                    print("Key Generated")
        else:
            cls.genSalt()
            cls.keygen(pw)
            print("Key Generated")
            time.sleep("5")
            os.system("cls")
        
    @classmethod        
    def genSalt(cls):
        with open("./salt", "wb") as saltf:
            saltf.write(f"{os.urandom(16)}".encode())

    @classmethod
    def loadKey(cls):
        with open("./key", "rb") as load:
            key = load.read()
        return key
    
    @classmethod
    def auth(cls,key):
        if os.path.exists("./key") == False:
            print("Generate Your Key First!")
            time.sleep()
            os.system("cls")
        mainpass = getpass.getpass("Main Password: ")
        if cls.keygen(mainpass) == key:
            print("Authorization Complete!")
            fer = Fernet(key)
            return fer
        else:
            print("Incorrect Password! Closing in 5 Seconds!")
            time.sleep(5)
            os.system("cls")
            quit()
    
    @classmethod
    def addPassword(cls,Fer):
        acc = input("Site/App: ")
        username = input("Username: ")
        passw = getpass.getpass("Password: ", "*")
        with open("logs.db", "a") as logs:
            logs.write(acc+"|"+username+"|"+Fer.encrypt(passw.encode()).decode()+"\n")
        print("Successfully Added the Password")
        time.sleep(3)
        os.system("cls")

    @classmethod 
    def view(cls, fer):
        with open('./logs.db', 'r', encoding='utf-8') as logs:
            for i in logs:
                data = i.rstrip()
                acc,user,pwd = data.split('|')
                print("Site/App:", acc, "    " "Username:", user, "   ", "Password:", fer.decrypt(pwd.encode()).decode())
            input("Press Any Key to Return to Menu")
            os.system("cls")