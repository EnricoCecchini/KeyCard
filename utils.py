import os
import json
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
        mainScreen()

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

def createJson(path):
    passwordDB = {}
    passwordDB['account'] = {}

    passwordDB = json.dumps(passwordDB)

    #db = json.loads(passwordDB)

    f = open(f"{path}\passwords.json", 'wb')
    f.write(bytes(passwordDB, 'utf-8'))
    f.close

def mainScreen():
    #os.system('cls')
    print("""
            _  __           ____              _  
            | |/ /___ _   _ / ___|__ _ _ __ __| | 
            | ' // _ \ | | | |   / _` | '__/ _` | 
            | . \  __/ |_| | |__| (_| | | | (_| | 
            |_|\_\___|\__, |\____\__,_|_|  \__,_| 
                    |___/           
            """)
    
def storeNewPassword(key):
    path = getPath()
    while True:
        os.system('cls')
        mainScreen()

        url = input('Platform URL: ')
        user = input('New User: ')
        password = input('Password: ')
        passwordConfirmation = input('Confirm password: ')

        if password == passwordConfirmation:
            break
        else: 
            print('Passwords don\'t match, try again')
    
    userEnrcypted, passwordEncrypted = encryption.encrypt(user, password, key)

    credentials = {
                "Platform": url,
                "User": userEnrcypted.decode('UTF-8'),
                "Password": passwordEncrypted.decode('UTF-8')
            }

    with open(f"{path.strip()}\passwords.json", 'r+') as jsonFile:
        f = json.load(jsonFile)

        #size = len(f)

        # f[f"account{size+1}"]["Platform"] = credentials["Platform"]
        # f[f"account{size+1}"]["User"] = credentials["User"]
        # f[f"account{size+1}"]["Password"] = credentials["Password"]

        # json.dump(f, jsonFile, indent=4)

        f.update(credentials)

        passwordDB = json.dumps(f)


        #passwordDB = json.load(jsonFile)

    print(passwordDB)
    print(type(passwordDB))

    f = open(f"{path}\passwords.json", 'wb')
    f.write(bytes(passwordDB, 'utf-8'))
    f.close

    # with open('passwords.json') as file:
    #     json.dump(credentialsJSON, file)

    # if not os.path.exists(f"{path.strip()}\passwords.json"):
    #     print(getPath()+'\passwords.json')
    #     credentialsJSON = json.dumps(credentials, indent=4)

    #     with open(f"{path.strip()}\passwords.json", 'w') as file:
    #         json.dump(credentialsJSON, file)
    # else:
    #     print("Adding new password")
    #     print(f"{path.strip()}\passwords.json")

    #     jsonFile = json.loads(f"{path.strip()}\passwords.json")
    #     passwordDB = json.loads(jsonFile)
    #     print(type(passwordDB))

    #     passwordDB = jsonFile.append(credentials)
    #     with open(f"{path.strip()}\passwords.json", 'w') as file:
    #         json.dump(passwordDB, file)

    input('Press ENTER to continue...')

def printPassword(key, platform):
    path = getPath()
    with open(f"{path.strip()}\passwords.json", 'r+') as jsonFile:
        passwordDB = json.load(jsonFile)
        
        #for credentials in passwordDB:
            #user, password = encryption.decrypt(credentials["User"], credentials["Password"], key)
            #print(user, password)
            #print(credentials)
        #user, password = encryption.decrypt(passwords['User'], passwords['Password'], key)
        print(passwordDB)
        print(type(passwordDB))

        #passwords = json.loads(passwordDB)
        #print(passwords)
        #print(type(passwords))
        #print(passwords['url'], user, password)
    
    input('Press ENTER to continue...')

def updatePassword(key):
    pass

def backupPasswords():
    pass