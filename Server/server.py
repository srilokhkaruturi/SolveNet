from datetime import datetime
import socket
import sys

## logging
def create_log_message(action, message):
    current_date = datetime.today().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime("%H:%M")
    return "{} [{}] {} {}\n".format(current_date, action, current_time, message)
logFile = open("log.txt", 'a')

s = socket.socket()
port = 6000
s.bind(('', port))
s.listen(5)
print("[Server] Server Socket is listening on PORT:", port)

while (True):
    c, addr = s.accept()

    # log new connection
    print('[server] Received connection from', addr)
    create_log_message("[server] Received connection from", addr)

    # send welcome message
    message = "Thank you for connecting."
    c.send(message.encode())
    print(c.recv(1024).decode())

    if(c.recv(1024).decode() == "exit"):

        print(" Shutting down server.")
        c.close()
        break

    c.send(message.encode("utf-8"))
    create_log_message("[server][Sending -> %s] %s" % (str(addr), message))

    # recv message
    received_message = s.recv(1024).decode()
    print("[server][Received from -> %s] %s" % (str(addr), received_message))
    create_log_message("[server][Received from -> %s] %s" % (str(addr), received_message))

    print("[server] Shutting down server.")
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



# initial_message = "Logging Started."
# logFile.write(create_log_message(action="START",message=initial_message))

# action, message = sys.stdin.readline().rstrip().split(" ", 1)

# while action != 'QUIT':
#     logFile.write(create_log_message(action=action, message=message))
#     # read the next action & message from the driver via standard input
#     action, message = sys.stdin.readline().rstrip().split(" ", 1)

# closing_message = "Logging Stopped."
# logFile.write(create_log_message(action="STOP", message=closing_message))

# # close the log file 
# logFile.close()
