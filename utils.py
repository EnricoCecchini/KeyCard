import os
import json
import encryption
import shutil
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

    credentials = read.split(b',')
    user, password = credentials[0], credentials[1]

    return user, password

# Get login data PATH from config file
def getPath():
    f = open("config.txt", 'r')
    path = f.read()

    return path

# Create new JSON file
def createJson(path, credentials):
    accounts = {
        "accounts": [
            {
                "Platform": credentials['Platform'],
                "User": credentials['User'],
                "Password": credentials['Password'],
            }
        ]
    }

    with open('passwords.json', 'w') as file:
        json.dump(accounts, file, indent=4)

# Print Logo
def mainScreen():
    os.system('cls')
    print("""
            _  __           ____              _  
            | |/ /___ _   _ / ___|__ _ _ __ __| | 
            | ' // _ \ | | | |   / _` | '__/ _` | 
            | . \  __/ |_| | |__| (_| | | | (_| | 
            |_|\_\___|\__, |\____\__,_|_|  \__,_| 
                    |___/           
            """)

# Store new account data in JSON
def storeNewPassword(key):
    path = getPath()
    while True:
        os.system('cls')
        mainScreen()

        # Get account data from user to store
        url = input('Platform URL: ')
        user = input('New User: ')
        password = input('Password: ')
        passwordConfirmation = input('Confirm password: ')

        if password == passwordConfirmation and user != '' or password != '' or url != '':
            break
        else: 
            print('Passwords don\'t match, try again')
    
    # Encrypt user and password
    userEnrcypted, passwordEncrypted = encryption.encrypt(user, password, key)

    # Store credentials in dictionary
    credentials = {
                "Platform": url,
                "User": userEnrcypted.decode('UTF-8'),
                "Password": passwordEncrypted.decode('UTF-8')
            }
    
    # Create new JSON if no file exists or if empty
    if not os.path.isfile(f"{path}\passwords.json") or os.stat(f"{path}\passwords.json").st_size == 0:
        createJson(path, credentials)   

    else:
        # Open JSON to read data already stored
        with open(f"{path.strip()}\passwords.json") as jsonFile:
            accounts = json.load(jsonFile)
            print(type(accounts))

            jsonFile.close()

        # Open JSON and store updated password data
        with open('passwords.json', 'w') as jsonFile:
            temp = accounts["accounts"]
            temp.append(credentials)

            json.dump(accounts, jsonFile, indent=4)

    input('Press ENTER to continue...')

# Print Account Infor stored in JSON
def searchPlatformAccounts(key, platform):
    mainScreen()
    print('Accounts for:', platform, '\n')
    path = getPath()
    
    try:
        # Load JSON
        with open(f"{path.strip()}\passwords.json") as jsonFile:
            passwordDB = json.load(jsonFile)

            for account in passwordDB['accounts']:

                if platform == account['Platform']:
                    user, password = encryption.decrypt(bytes(account['User'], 'UTF-8'), bytes(account['Password'], 'UTF-8'), key)
                
                    # Print account data
                    print('Platform:', account['Platform'])
                    print('Username:', user)
                    print('Password:', password) 

                    print('')

    except FileNotFoundError:
        print("KeyError - No Passwords stored")
    
    input('Press ENTER to continue...')

# Print Account info for specific platform stored in JSON
def printAllAccounts(key):
    mainScreen()
    print('Accounts:')
    path = getPath()
    
    try:
        # Load JSON
        with open(f"{path.strip()}\passwords.json") as jsonFile:
            passwordDB = json.load(jsonFile)

            for account in passwordDB['accounts']:

                user, password = encryption.decrypt(bytes(account['User'], 'UTF-8'), bytes(account['Password'], 'UTF-8'), key)
            
                # Print account data
                print('Platform:', account['Platform'])
                print('Username:', user)
                print('Password:', password) 

                print('')

    except FileNotFoundError:
        print("KeyError - No Passwords stored")
    
    input('Press ENTER to continue...')

def updatePassword(key):
    pass

def backupPasswords():
    path = getPath()
    backupPath = input('Backup Path: ')

    if os.path.exists(backupPath):
        backup = [f'{path}\key.txt', f'{path}\passwords.json']

        for file in backup:
            shutil.copy(file, backupPath)
    
        print('Files have been backed up at: ', backupPath)
    
    else:
        print('Invalid Path')

    input('Press ENTER to continue...')