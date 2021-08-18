# LunchBox
Locally stored password Manager

Python program to store account data locally in a JSON file. Account User and Passwords are encrypted using the Fernet cryptography module. A unique key is generated when the program is first run, which is required to decrypt account data.

*Only Username and Password are encrypted, not the platform each account data belongs to*

Features not implemented yet:

-Update existing account data

-Backup password and key files in new directory


Instructions:

Copy PATH to store passwords in config.txt

Run PasswordManager.py

Create user and password for program

Add new Account data (a JSON file is generated on first run which will store encrypted account data)

