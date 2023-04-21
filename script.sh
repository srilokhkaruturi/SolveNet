#!/bin/bash

#start server
x-terminal-emulator -e python ./Server/server.py

#start each client
for i in $(seq 1 3)
do
	x-terminal-emulator -e python ./Client/client.py
done



