import subprocess
import time

y = input("Enter desired number of clients: ")

subprocess.Popen(["python3", "./Server/server.py"])


for x in range(0 , int(y)):
	subprocess.Popen(["python3", "./Client/client.py"])
