#!/usr/bin/python2.7
import sys
import socket
import time

ip = "161.47.68.144"
port = 2112
retry = 1
delay = 1
timeout = 2

def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False

def checkHost(ip, port):
    ipup = False
    for i in range(retry):
        if isOpen(ip, port):
            ipup = True
            break
        else:
            time.sleep(delay)
    return ipup

if checkHost(ip, port):
    print ip + " port " + str(port) + u" is \u001b[32;1mUP!\u001b[0m"
else:
    print ip + " port " + str(port) + u" is \u001b[31;1mDOWN!\u001b[0m"
