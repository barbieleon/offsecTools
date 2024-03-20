#!/usr/bin/python3

import socket,sys,codecs,re

if len(sys.argv) !=3:
    print("SMTP BRUTE FORCE")
    print("How to use: ./BarbieSMTPBrute.py + IP + userlist")
    print("E.g.: ./BarbieSMTPBrute.py + 172.16.1.50 users.txt")
    sys.exit(0)




#Opening the file containing the users
file = open(sys.argv[2], "rb")
for lines in file:
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((sys.argv[1],25))
    banner = tcp.recv(1024).replace(b"\r\n",b"")
    
    tcp.send(b"VRFY "+lines)
    users = tcp.recv(1024).replace(b"\r\n",b"").decode("utf-8")
    if re.search("252",users):
        print("User found: "+users.strip("252 2.0.0"))