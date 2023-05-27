import socket
import time
import fcntl, os
import errno
import sys
 #
 #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 #s.connect(("challenges.404ctf.fr", 30980))
 #while True:
     #time.sleep(0.2)
     #try:
         #data = s.recv(4096).decode()
         #if not data:
             #break
         #print(data)
 #
         #s.send((str(value) + "\n").encode("utf8"))
     #except socket.error as e:
         #if e.errno == errno.ECONNRESET:
             #print("Connection reset by peer")
         #else:
             #print("Socket error:", e)
         #break
 #s.close()
 #
