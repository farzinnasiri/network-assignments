import sys
import time
import random
from socket import *

'''
run the command: "python pinger.py serve" to run the server 
run the command: "python pinger.py ping" to ping the server

default port number is 8000 
'''


def main():
    # initializing
    arg = sys.argv[1]
    if arg == "serve":
        server = Server(8000, 'localhost')
        server.run()
    elif arg == "ping":
        client = Client(8000, 'localhost')
        client.run()
    else:
        print("Command not found...")


# client class for pinging the server

class Client:
    def __init__(self, port, host):
        self.port = port
        self.host = host

    def run(self):
        client_socket = socket(AF_INET, SOCK_DGRAM)
        # set 1 second time out
        client_socket.settimeout(1)

        print("PINGING", self.host, ":", self.port)
        for i in range(10):
            print("------------------------------------------------------------------------------------")
            message = "PING"
            print(message)

            # start timer for rtt
            start_time = int(round(time.time() * 1000000))

            # sending ping message to server
            client_socket.sendto(message.encode('utf-8'), (self.host, self.port))

            try:
                # getting the response from server
                response, _ = client_socket.recvfrom(1024)
                end_time = int(round(time.time() * 1000000))
                # calculating the rtt
                rtt = end_time - start_time
                print("PONG", " rtt:", rtt, "\u03BCs", "seq_num:", i + 1)

            except timeout:
                # if no pong message came after 1 second then request is timed out
                print("REQUEST TIMED OUT", "seq_num:", i + 1)
            time.sleep(1)


# server class

class Server:
    def __init__(self, port, host):
        self.port = port
        self.host = host

    def run(self):

        server_socket = socket(AF_INET, SOCK_DGRAM)
        server_socket.bind((self.host, self.port))

        print("Server is running on", self.host, ":", self.port)
        while True:
            chance = random.randint(0, 10)
            # getting a ping message
            message, addr = server_socket.recvfrom(1024)

            # 30 percent chance of failure ( dropping packets)
            if chance > 3:
                # resending th same message
                server_socket.sendto(message, addr)


if __name__ == '__main__':
    main()
