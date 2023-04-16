import socket
import sys
import random
import requests


class Client:
    def __init__(self, destination_ip, destination_port):
        self.destination_ip = destination_ip
        self.destination_port = destination_port
        self.socket = socket.socket()
        self.name = Client.get_random_name()

    def connect(self):
        # CONNECT
        self.socket.connect((self.destination_ip, self.destination_port))

        # RECEIVE INITIAL SERVER ACK
        server_ack = self.socket.recv(1024).decode()
        print("[Client %s] %s" % (self.name, server_ack))

        # SEND NAME
        self.send(self.name)

        # RECEIVE NAME ACK
        name_server_ack = self.socket.recv(1024).decode()
        print("[Client %s] %s" % (self.name, name_server_ack))

        # FINISH

    def send(self, msg: str):
        self.socket.send(msg.encode())

    def recieve(self):
        return self.socket.recv(1024).decode()

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
                first += " " + b1 + " " + str(a) + " " + a1 + " " + str(b)
                return str(first)
            else:
                return str(first)

    @staticmethod
    def get_random_name():
        response = requests.get("https://randomuser.me/api/")
        data = dict(response.json())
        return (data["results"][0])["name"]["first"]


def client():
    client = Client("127.0.0.1", 6000)
    client.connect()

    while (True):
        # sending
        sending_message = Client.generate()
        client.send(sending_message) # CHANGE THIS IF YOU WANT TO TEST WITH THE SAME EXPRESSION
        print("Sending:", sending_message)

        # recieving
        recieved_message = client.recieve()
        print("Received:", recieved_message)


client()
