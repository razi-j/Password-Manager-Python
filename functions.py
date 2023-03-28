import base64
import os
import getpass
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC # Password Based Key Derive Function
from cryptography.fernet import Fernet

class Pwman:
    @classmethod
    def keygen(cls,pw):
        password = pw.encode()
        with open("salt", "rb") as saltf:
            salt = bytes(saltf.read())
        print("Generating Key")
        kdf = PBKDF2HMAC(
                    algorithm=hashes.SHA256,
                    salt=salt,
                    length=32,
                    iterations=480000
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        with open("./key", "wb") as keyf:
            keyf.write(key)
        print("Key Generated")

    @classmethod
    def buildkey(cls, pw):
        if os.path.exists("./key"):
            ch = input("Key Already Exists!\nGenerate a new key?(y/n) ")
            if ch.lower() != "y" and ch.lower() != "n":
                print("Invalid Input")
            else:
                if ch.lower()=="y":
                    cls.genSalt()
                    cls.keygen(pw)
        else:
            cls.genSalt()
            cls.keygen(pw)
        
    @classmethod        
    def genSalt(cls):
        with open("salt", "wb") as saltf:
            saltf.write(f"{os.urandom(16)}".encode())
        
