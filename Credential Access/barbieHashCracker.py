#!/usr/bin/python3
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import sys,crypt

PURPLE = "\33[91m"
ENDCOLOR = "\033[0m"

def display_banner():
    banner_text = ''' 



                              .______        ___      .______      .______    __   _______                                      
                              |   _  \      /   \     |   _  \     |   _  \  |  | |   ____|                                     
                              |  |_)  |    /  ^  \    |  |_)  |    |  |_)  | |  | |  |__                                        
                              |   _  <    /  /_\  \   |      /     |   _  <  |  | |   __|                                       
                              |  |_)  |  /  _____  \  |  |\  \----.|  |_)  | |  | |  |____                                      
                              |______/  /__/     \__\ | _| `._____||______/  |__| |_______|                                     
                                                                                                                                
                                                                                                                                
                                                                                                                                
 __    __       ___           _______. __    __       ______ .______           ___        ______  __  ___  _______ .______      
|  |  |  |     /   \         /       ||  |  |  |     /      ||   _  \         /   \      /      ||  |/  / |   ____||   _  \     
|  |__|  |    /  ^  \       |   (----`|  |__|  |    |  ,----'|  |_)  |       /  ^  \    |  ,----'|  '  /  |  |__   |  |_)  |    
|   __   |   /  /_\  \       \   \    |   __   |    |  |     |      /       /  /_\  \   |  |     |    <   |   __|  |      /     
|  |  |  |  /  _____  \  .----)   |   |  |  |  |    |  `----.|  |\  \----. /  _____  \  |  `----.|  .  \  |  |____ |  |\  \----.
|__|  |__| /__/     \__\ |_______/    |__|  |__|     \______|| _| `._____|/__/     \__\  \______||__|\__\ |_______|| _| `._____|


BarbieHashCracker V1.0
Coded by Barbie Leon

    '''
    print(f"{PURPLE}{banner_text}{ENDCOLOR}")
display_banner()


if len(sys.argv) <=1:
    print("How to use: ./barbieCrack.py + passwords")
else:
    #Input to capture the salt
    targetHash = input("Enter the target hash: ")
    salt = input("Enter the Salt: ")
    passwordFile = sys.argv[1]


    #Opening a custom file with passwords
    with open(passwordFile, "r") as file:
        for passwords_in_file in file:
            password = passwords_in_file.strip()
            hashed_password = crypt.crypt(password, salt)
            if(targetHash == hashed_password):
                print("Original password: ", password, "Hashed: ",hashed_password)