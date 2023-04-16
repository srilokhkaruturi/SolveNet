from datetime import datetime
import socket
import sys
import threading

# logging


def create_log_message(action, message):
    current_date = datetime.today().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime("%H:%M")
    return "{} [{}] {} {}\n".format(current_date, action, current_time, message)


class clientRequest:
    connectionTime = ""
    disconnectionTime = ""
    userId = ""


def clientThread(ip, port):
    print(";-;")


def calculateLine(line):
    stringList = line.split(" ")
    solution = int(stringList[0])
    for x in range(1, len(stringList), 2):
        if (x % 2 == 1):
            if (stringList[x] == "+"):
                solution += int(stringList[x+1])
            elif (stringList[x] == "-"):
                solution -= int(stringList[x + 1])
            elif (stringList[x] == "/"):
                solution /= int(stringList[x + 1])
            elif (stringList[x] == "*"):
                solution *= int(stringList[x + 1])
            elif (stringList[x] == "%"):
                # ISSUE WITH FLOAT/INTS/EXPONENTS
                solution = solution % int(stringList[x + 1])
            elif (stringList[x] == "^"):
                solution = solution ** int(stringList[x + 1])
    return solution


s = socket.socket()
port = 6000
s.bind(('', port))
s.listen(5)
print("[Server] Server Socket is listening on PORT:", port)

logFile = open("log.txt", 'a')

while (True):
    # TODO: Change C -> Client??
    c, addr = s.accept()
    Ip, port = addr
    # x = threading.Thread(target= ,  args=(str(Ip),str(port),)
    # log new connection
    # print(str(Ip) + " " + str(port))
    print('[server] Received connection from', addr)
    create_log_message("[server] Received connection from", addr)

    # send welcome message
    message = "Thank you for connecting."
    c.send(message.encode())

    # receive client name and send name ack
    name = c.recv(1024).decode()
    message = "Hello " + name + "!"
    c.send(message.encode())

    while (True):
        expression = c.recv(1024).decode()
        if (expression == "exit"):
            print("[server] Shutting down server.")
            c.close()
            break
        else:
            result = str(calculateLine(expression))
            c.send(result.encode())

            print("[server][Sending -> %s]" %
                  result)

            # create_log_message("[server][Received from -> %s] %s" %
            #                    (str(addr), expression))

    print("[server] Shutting down server.")
    c.close()
    break


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
