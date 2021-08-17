import os
import encryption
from cryptography.fernet import Fernet

# Generate key for encryption
def makeKey(path):
    key = Fernet.generate_key()
    file = open('key.txt', 'wb')
    file.write(key)
    file.close

# Read key from file
def readKey(path):
    with open('key.txt', 'rb') as f:        
        key = f.read()
    
    return key

# Login user
def login(encryptedUser, encryptedPassword, key):
    attempts = 3

    while attempts > 0:
        user = input("User: ")
        password = input("Password: ")

        # Decrypt User and Password for validation
        validUser, validPassword = encryption.decrypt(encryptedUser, encryptedPassword, key)

        # Check LogIn Credentials
        if user == validUser and password == validPassword:
            return True
        else:
            print("Wrong Password!")
            print(validUser + validPassword)
            attempts -= 1

    print('Access Denied')
    return False

# Get login data from new user
def getLogin():
    while True:
        user = input("New User: ")
        password = input("Password: ")
        confirmPassword = input("Confirm password: ")

        if password == confirmPassword:
            break
    
    #user, password = encryption(user, password)
    return user, password

# Store login credentials in file
def storeLogin(user, password, path, key):
    loginFilePath = f"{path.strip()}\login.txt"
    print(loginFilePath)
    f = open(loginFilePath, 'wb')

    # Encrypt LogIn user and password before saving them in file
    encryptedUser, encryptedPassword = encryption.encrypt(user, password, key)
    f.write(encryptedUser)
    f.write(b',')
    f.write(encryptedPassword)
    f.close

# Read Login credentials from login file
def readLogin(path):
    loginFilePath = f"{path.strip()}\login.txt"
    with open(loginFilePath, 'rb') as f:        
        read = f.read()

    #print("Read:", read)
    credentials = read.split(b',')
    #print("Credentials:", credentials)
    user, password = credentials[0], credentials[1]

    return user, password

# Get login data PATH from config file
def getPath():
    f = open("config.txt", 'r')
    path = f.read()

    return path

def mainScreen():
    print("""
            _  __           ____              _  
            | |/ /___ _   _ / ___|__ _ _ __ __| | 
            | ' // _ \ | | | |   / _` | '__/ _` | 
            | . \  __/ |_| | |__| (_| | | | (_| | 
            |_|\_\___|\__, |\____\__,_|_|  \__,_| 
                    |___/           
            """)

def storePassword():
    pass

def readPassword():
    pass

def printPassword():
    pass

def updatePassword():
    pass