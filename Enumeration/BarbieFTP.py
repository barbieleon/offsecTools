#!/usr/bin/python3
import sys
import socket


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((sys.argv[1],int(sys.argv[2])))

print("PRINTING BANNER")
banner = tcp.recv(1024)
print (banner.replace(b"\r\n",b""))


print("SENDING THE USER")
tcp.send(str.encode("USER ftp\r\n" + "\r\n"))
user = tcp.recv(1024)
print (user.replace(b"\r\n",b""))

print("SENDING THE PASSWORD")
tcp.send(str.encode("PASS ftp\r\n"))
password = tcp.recv(1024)
print (password.replace(b"\r\n",b""))


print("SENDING COMMANDS")
tcp.send(str.encode("HELP\r\n"))
command = tcp.recv(2048)
print (command.replace(b"\r\n",b""))