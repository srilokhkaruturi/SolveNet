import socket
import sys

s = socket.socket()
host = socket.gethostname()
port = 6000

s.connect((host, port))

message = s.recv(1024).decode()

while (True):
    expression = input("Input: ")

    # send message
    s.send(expression.encode())
