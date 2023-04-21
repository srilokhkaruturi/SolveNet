import subprocess
import time

print("Enter desired number of clients")
y = input()

subprocess.Popen(["python3", "./Server/server.py"])


for x in range(0 , int(y)):
	subprocess.Popen(["python3", "./Client/client.py"])
