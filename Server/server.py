import socket
import sys

s = socket.socket()
print("Socket successfully created")

port = 6000
counter =0
s.bind(('', port))
print("socket binded to %s" % (port))
s.listen(5)
print("socket is listening")

while(True):
    c, addr = s.accept()
    print('Got connection from', addr)

    message = "Thank you for connecting."
    c.send(message.encode())
    print(c.recv(1024).decode())

    if(c.recv(1024).decode() == "exit"):

        print(" Shutting down server.")
        c.close()
        break


def calculateLine(line):
    stringList = line.split("")
    solution= int(stringList[0])
    for x in range(1 , len(stringList) , 2):
        if(x % 2 == 1):
            if(stringList[x]== "+"):
                solution += int(stringList[x+1])
            elif (stringList[x] == "-"):
                solution -= int(stringList[x + 1])
            elif (stringList[x] == "/"):
                solution /= int(stringList[x + 1])
            elif (stringList[x] == "*"):
                solution *= int(stringList[x + 1])
            elif (stringList[x] == "%"):
                solution = solution % int(stringList[x + 1])
            elif (stringList[x] == "^"):
                solution = solution ^ int(stringList[x + 1])
    return solution

