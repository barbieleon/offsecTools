#!/usr/bin/python3

import sys,crypt

if len(sys.argv) <=1:
    print("BarbieHashCracker")
    print("How to use: ./barbieCrack.py + passwords")
else:
    #Input to capture the salt
    salt = input("Enter the Salt: ")
    passwordFile = sys.argv[1]


    #Opening a custom file with passwords
    with open(passwordFile, "r") as file:
        for passwords_in_file in file:
            password = passwords_in_file.strip()
            hashed_password = crypt.crypt(password, salt)
            print("Original password: ", password, "Hashed: ",hashed_password)