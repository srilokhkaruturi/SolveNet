#!/bin/bash

#start server
x-terminal-emulator -e python ./Server/server.py

#wait for server to start
sleep 2

#start each client
echo "Enter in your desired number of clients \n"
read clientCount

for i in $(seq 1 $clientCount)
do
	x-terminal-emulator -e python ./Client/client.py
done



