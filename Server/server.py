# import statements
from datetime import datetime
import socket

class Server:
    def __init__(self, port, file_name):
        self.socket = socket.socket()
        self.log_file = None
        self.client = None
        # Bind this socket to the specified port on all network interfaces of the machine
        self.socket.bind(("", port))
        # Specify the maximum number of connections that this socket can service
        self.socket.listen(5)

    def accept_connection(self):
        # Accept connection request
        self.client, address = self.socket.accept()
        print('[Server] Received connection from', address)
        # Get connection time
        current_date = datetime.today().strftime('%Y-%m-%d')
        current_time = datetime.now().strftime("%H:%M")
        # Get the full time with date
        connection_time = current_date + ' ' + current_time
        # Extract client's IP address and port number
        ip, port = address

        return ip, port, connection_time
        
    def close_connection(self):
        print("[Server] Shutting down connection.")
        self.client.close()

    def send(self, message):
        self.client.send(message.encode())

    def receive(self):
        return self.client.recv(1024).decode()
    
    def open_file(self, file_name):
        self.log_file = open(file_name + '.txt', 'a')

    def close_file(self):
        self.log_file.close()

    def log_message(self, ip, port, name, time):
        self.log_file.write('Client Name: {}, Connection Time: {}, IP Address: {}, Port Number: {}\n'.format(name, time, ip, port))
    
    def calculate_expression(self, expression):
        stringList = expression.split(" ")
        result = int(stringList[0])
        for x in range(1, len(stringList), 2):
            if (x % 2 == 1):
                if (stringList[x] == "+"):
                    result += int(stringList[x+1])
                elif (stringList[x] == "-"):
                    result -= int(stringList[x + 1])
                elif (stringList[x] == "/"):
                    result /= int(stringList[x + 1])
                elif (stringList[x] == "*"):
                    result *= int(stringList[x + 1])
                elif (stringList[x] == "%"):
                    # ISSUE WITH FLOAT/INTS/EXPONENTS
                    result = result % int(stringList[x + 1])
                elif (stringList[x] == "^"):
                    result = result ** int(stringList[x + 1])
        return result


def server():
    # Variables
    port = 6000
    file_name = 'log'

    # Create a new server instance
    server = Server(port=port, file_name=file_name)
    print('[Server] Server socket is listening on PORT:', port)

    # Open the log file for appending
    server.open_file(file_name) 

    while (True):
        # Retrieve client adress = (IP address, port number)
        ip, port, time = server.accept_connection()
    
        # Send initial server acknowledgement
        message = "Thank you for connecting."
        server.send(message)

        # Receive client name and send name ack
        name = server.receive()
        message = "Hello " + name + "!"
        server.send(message)

        # Log the client details
        server.log_message(ip, port, name, time)

        while (True):
            expression = server.receive()

            if (expression == "exit"):
                server.close_connection()
                break
            else:
                result = str(server.calculate_expression(expression))
                server.send(result)

            print("[Server][Sending -> %s]" % result)
    
        
        print("[Server] Shutting down connection.")
        break
    
    server.close_file()

server()

