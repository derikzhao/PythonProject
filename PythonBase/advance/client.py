# encoding:UTF-8

import socket

s = socket.socket()
host = socket.gethostname() #ip
port = 9084

s.connect((host, port))

print "connect server"

while True:
    cmd = raw_input("send messages：")
    s.sendall(cmd)
    print s.recv(1024)

s.close()
