#! /usr/bin/env python
# Written by Joshua Jordi

import socket

sock = socket.socket()
ip = socket.gethostbyname('www.google.com')
print(ip)
sock.connect((ip, 80))
sock.close()
