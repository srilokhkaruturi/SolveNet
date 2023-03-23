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
    c.send(message.encode("utf-8"))

    print(" Shutting down server.")
    c.close()
    break