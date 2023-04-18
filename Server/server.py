# import statements
from datetime import datetime
import threading
import socket

class Server:
    def __init__(self, port, file_name):
        self.socket = socket.socket()
        self.log_file = None
        # Bind this socket to the specified port on all network interfaces of the machine
        self.socket.bind(("", port))
        # Specify the maximum number of connections that this socket can service
        self.socket.listen(5)

    def accept_connection(self):
        # Accept connection request
        client_socket, address = self.socket.accept()
        print('[Server] Received connection from', address)
        # Get connection time
        connection_time = datetime.now()
        
        # Extract client's IP address and port number
        ip, port = address
        # Return client details
        return client_socket, ip, port, connection_time
        
    def close_connection(self, client_socket, client_name, connection_time):
        # Get disconnection time
        disconnection_time = datetime.now()
        # Calculate the duration connected
        duration = disconnection_time - connection_time
        # Close the socket connection
        client_socket.close()
        print("[Server] Shutting down the connection for Client {}.".format(client_name))
        
        return disconnection_time, duration

    def send(self, client_socket, message):
        client_socket.send(message.encode())

    def receive(self, client):
        return client.recv(1024).decode()
    
    def open_file(self, file_name):
        self.log_file = open(file_name + '.txt', 'a')

    def close_file(self):
        self.log_file.close()

    def log_message(self, ip, port, name, time, action, duration=""):
        formatted_time = time.strftime("%Y-%m-%d%H:%M")
        if action == "CONNECT":
            self.log_file.write('[{}] Client Name: {}, Connection Time: {}, IP Address: {}, Port Number: {}\n'.format(action, name, formatted_time, ip, port))
        else:
            self.log_file.write('[{}] Client Name: {}, Disconnection Time: {}, IP Address: {}, Port Number: {}, Duration: {}\n'.format(action, name, formatted_time, ip, port, duration))
        
        self.log_file.flush()

    
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
                    result = result % int(stringList[x + 1])
                elif (stringList[x] == "^"):
                    result = result ** int(stringList[x + 1])
        return result

def handle_client_connection(server, client_socket, ip, port, connection_time):
    # Send initial server acknowledgement
    message = "Thank you for connecting."
    server.send(client_socket, message)

    # Receive client name and send name ack
    name = server.receive(client_socket)
    message = "Hello " + name + "!"
    server.send(client_socket, message)

    # Log the client details
    server.log_message(ip, port, name, connection_time, action="CONNECT")

    while (True):
        expression = server.receive(client_socket)
        # Print who has sent what request
        print("[Server] Received \" {} \" from Client {}".format(expression, name))

        if (expression == "exit"):
            disconnection_time, duration = server.close_connection(client_socket, name, connection_time)
            server.log_message(ip, port, name, disconnection_time, action="DISCONNECT", duration=duration)
            break
        else:
            result = str(server.calculate_expression(expression))
            server.send(client_socket, result)

        # Print the answer of the expression received from the client
        print("[Server] Sent \" {} \" as a result to Client {}".format(result, name))
    
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
        # Wait on new connection requests
        client_socket, ip, port, time = server.accept_connection()

        # Create a new thread for the incoming connection
        thread = threading.Thread(target=handle_client_connection, args=(server, client_socket, ip, port, time))
        thread.start()

server()

