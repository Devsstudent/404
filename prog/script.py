import socket
import time
import fcntl, os
import errno
import sys

def count_rino(nice):
    i = 0
    index = 0
    while 1:
        if (index == 0):
            index = nice.find("~c`°^)", index);
        else:
            index = nice.find("~c`°^)", index + 1);
        if (index == -1)  :
            break 
        else:
            i = i + 1
    return i

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("challenges.404ctf.fr", 31420))
while True:
    time.sleep(0.2)
    try:
        data = s.recv(4096).decode()
        if not data:
            break
        print(data)
        value = count_rino(data)
        print(value)
        s.send((str(value) + "\n").encode("utf8"))
    except socket.error as e:
        if e.errno == errno.ECONNRESET:
            print("Connection reset by peer")
        else:
            print("Socket error:", e)
        break
s.close()

