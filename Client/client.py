import socket
import sys
import random
#import names


class Client:
    def __init__(self, destination_ip, destination_port):
        self.destination_ip = destination_ip
        self.destination_port = destination_port
        self.socket = socket.socket()

    def connect(self):
        self.socket.connect((self.destination_ip, self.destination_port))
        message = self.socket.recv(1024).decode()
        print("[Client]", message)

    def send(self, msg: str):
        self.socket.send(msg.encode())
    def recieve(self):
        return self.socket.recv(1024).decode()
    @staticmethod
    def get_random_name():
        pass

    @staticmethod
    def generate():
        symbol = "+-*%^/"
        for x in range(0, 1):

            a = random.randint(0, 9)
            a1 = symbol[random.randint(0, 5)]
            b = random.randint(0, 9)

            first = str(a) + " " + a1 + " " + str(b)
            if (random.randint(0, 1)):
                b1 = symbol[random.randint(0, 5)]
                a = random.randint(0, 9)
                a1 = symbol[random.randint(0, 5)]
                b = random.randint(0, 9)
                first += " " +  b1 + " " + str(a)  + " "+ a1 + " " + str(b)
                return str(first)
            else:
                return str(first)


def client():
    client = Client("127.0.0.1", 6000)
    client.connect()

    while (True):
         expression = input("Input: ")

         # sending
         sending_message = client.generate()
         print(sending_message)
         client.send(sending_message)

         # receiving
         received_message = client.recieve()
         print(received_message)

client()
