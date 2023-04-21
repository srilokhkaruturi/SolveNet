README.txt
This project contains a simple multi-client server and client implementation for a math expression calculator. The server can handle multiple clients and solve their math expressions. The client will generate random math expressions and send them to the server for evaluation. The server keeps a log of client connections and disconnections with their respective durations.

Running: (running with two clients and one server per say)
Note: You can create as many instances of a client by running in 2.another terminal window.

1. ensure Python3 installed
2. Change directory to driver.py location
3. Run driver: python3 driver.py
4. Observe
5. Kill Server after clients are done: CTRL+C
6. Potentially need use ‘pkill python3’ in case log file is not loading or to run a second time.
7. Open log file in same location as driver.py.
8. Verify interaction



Files
driver.py
client.py
server.py
