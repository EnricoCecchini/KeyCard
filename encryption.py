from cryptography.fernet import Fernet


# Encrypt user and password
def encrypt(user, password, key):
    f = Fernet(key)

    encryptedUser = f.encrypt(bytes(user, 'utf-8'))
    encryptedPassword = f.encrypt(bytes(password, 'utf-8'))

    return encryptedUser, encryptedPassword


# decrypt user and password
def decrypt(encryptedUser, encryptedPassword, key):
    f = Fernet(key)

    user = f.decrypt(encryptedUser).decode('utf-8')
    password = f.decrypt(encryptedPassword).decode('utf-8')

    return user, password
