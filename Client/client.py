import socket
import random
import requests
import time

# Client class
class Client:
    def __init__(self, destination_ip, destination_port):
        self.destination_ip = destination_ip
        self.destination_port = destination_port
        self.socket = socket.socket()
        self.name = Client.get_random_name()

    def connect(self):
        # CONNECT
        self.socket.connect((self.destination_ip, self.destination_port))
        print("[Client {}] Sent a connection request to Server".format(self.name))

        # RECEIVE INITIAL SERVER ACK
        server_ack = self.socket.recv(1024).decode()
        print("[Client {}] Received \" {} \" from Server".format(self.name, server_ack))

        # SEND NAME
        self.send(self.name)

        # RECEIVE NAME ACK
        name_server_ack = self.socket.recv(1024).decode()
        print("[Client {}] Received \" {} \" from Server".format(self.name, name_server_ack))

        # FINISH

    # Sends message to server
    def send(self, msg: str):
        self.socket.send(msg.encode())

    # Recieves message from server
    def recieve(self):
        return self.socket.recv(1024).decode()

    # Generates a random mathematical expression to be sent to server to be solved
    @staticmethod
    def generate():
        # Symbol string is used to be able to choose an operator
        symbol = "+-*%^/"

        for x in range(0, 1):
            # a and b are a random integer for the expression, a1 is the operand
            a = random.randint(1, 9)
            a1 = symbol[random.randint(0, 5)]
            b = random.randint(1, 9)

            first = str(a) + " " + a1 + " " + str(b)

            # 50/50 chance for an extended expression
            if (random.randint(0, 1)):
                b1 = symbol[random.randint(0, 5)]
                a = random.randint(1, 9)
                a1 = symbol[random.randint(0, 5)]
                b = random.randint(1, 9)
                first += " " + b1 + " " + str(a) + " " + a1 + " " + str(b)
                return str(first)
            else:
                return str(first)

    # Gets random name from the api to represent the client name
    @staticmethod
    def get_random_name():
        response = requests.get("https://randomuser.me/api/")
        data = dict(response.json())
        return (data["results"][0])["name"]["first"]


# Main method
# Creates a Client class object and orchestrates the functionality of sending/receving math expressions to/from Server
def client():
    # Uses local host by default
    client = Client("127.0.0.1", 6000)
    client.connect()

    for i in range(5):

        # Wait 2-5 seconds randomly before sending a new request
        wait_time = random.uniform(2, 5)
        time.sleep(wait_time)

        # Send the auto-generated expression
        sending_message = Client.generate()

        print("[Client {}] Sent \" {} \" to the Server".format(client.name, sending_message))
        # Change this if you want to test with the same expression
        client.send(sending_message)

        # Receive the result
        recieved_message = client.recieve()
        print("[Client {}] Received \" {} \" from the Server".format(client.name, recieved_message))
    
    # Send exit message
    client.send('exit')


client()
