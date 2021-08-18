import json
import utils
import os

# Print option menu
def mainMenu():
    options = [1,2,3,4,5,6]
    choice = 0
    while True:
        print('1 - Add New Account \n2 - Print Platform Accounts \n3 - Print All Account Data\n4 - Update Password \n5 - Backup Passwords \n6 - Exit')
        choice = int(input('\nChoice: '))

        if choice in options:
            break
        else:
            print('Invalid Choice, try again!')
    
    return choice

# Get login and password location PATH
path = utils.getPath().strip()

# Generate key if it's first time running
if not os.path.isfile(f"{path}\key.txt"):        
    utils.makeKey(path)

key = utils.readKey(path)

# Generate Login data file if first time running
if not os.path.isfile(f"{path}\login.txt"):        
    user, password = utils.getLogin()
    utils.storeLogin(str(user), str(password), path, key)
    print(str(user))
    print(str(password))

# Get user and password for login
user, password = utils.readLogin(path)

os.system('cls')
#utils.mainScreen()

# Login
verified = utils.login(user, password, key)
os.system('cls')

# Show menu until program ends
choice = 0
while choice != 6 and verified:
    os.system('cls')
    utils.mainScreen()
    choice = mainMenu()

    if choice == 1:
        utils.storeNewPassword(key)
    elif choice == 2:
        platform = input('Platform: ')
        utils.searchPlatformAccounts(key, platform)
    elif choice == 3:
        utils.printAllAccounts(key)    
    elif choice == 4:
        utils.updatePassword(key)
    elif choice == 5:
        utils.backupPasswords()
    elif choice == 6:
        break
    else:
        print('Invalid choice, try again')

os.system('cls')
print('Goodbye...')

