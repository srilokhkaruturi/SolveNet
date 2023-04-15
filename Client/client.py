import socket
import sys
import random

s = socket.socket()
host = socket.gethostname()
port = 6000

s.connect((host, port))

message = s.recv(1024).decode()

def generate():
    symbol="+-*%^/"
    for x in range(0, 1000):

        a = random.randint(0,9)
        a1 = symbol[random.randint(0,5)]
        b = random.randint(0,9)

        first = str(a) + a1 + str(b)
        if(random.randint(0,1)):
            b1 = symbol[random.randint(0, 5)]
            a = random.randint(0, 9)
            a1 = symbol[random.randint(0, 5)]
            b = random.randint(0, 9)
            first+= b1 + str(a) + a1 + str(b)
            print(first)
        else:
            print(first)

while (True):
    expression = input("Input: ")

    # send message
    s.send(expression.encode())
