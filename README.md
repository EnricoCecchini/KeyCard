# KeyCard
Locally stored password Manager

Python program to store account data locally in a JSON file. Account User and Passwords are encrypted using the Fernet cryptography module. A unique key is generated when the program is first run, which is required to decrypt account data.

*Only Username and Password are encrypted, not the platform each account data belongs to*.



**Instructions:**

1. Paste PATH to store passwords in config.txt

2. Run KeyCard.py

3. Create user and password for program

4. Add new Account data (a JSON file is generated on first run which will store encrypted account data)



**Bonus:**

You may have your login info stored somewhere else as long as you specify the desired directory inside an *'config.txt'* file.



*This program requires the cryptography module to operate*.

