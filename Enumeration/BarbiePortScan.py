#!/usr/bin/python3

import sys,socket

if len(sys.argv) <=1:
    print("Barbie PORT SCAN")
    print("How to use: ./BarbiePortScan.py 172.16.1.5")
else:
    for port in range(1,65535):
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if mysocket.connect_ex((sys.argv[1],port)) == 0:
            print("Open port",port)
            mysocket.close()
        else:
            #print("Closed Port",port)
            mysocket.close()