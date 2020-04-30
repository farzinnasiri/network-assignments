import sys
import time
import random
from socket import *

'''
run the command: "python heartbeat.py server" to run the server 
run the command: "python heartbeat.py client" to run the client

default port number is 8000 
'''


def main():
    arg = sys.argv[1]
    if arg == "server":
        server = Server(8000, 'localhost')
        server.run()
    elif arg == "client":
        client = Client(8000, 'localhost')
        client.run()
    else:
        print("Command not found...")


class Client:
    def __init__(self, port, host):
        self.port = port
        self.host = host

    def run(self):
        client_socket = socket(AF_INET, SOCK_DGRAM)

        print("Client is running on", self.host, ":", self.port)
        seq_num = 0
        while True:
            chance = random.randint(0, 10)
            # dropping packets with 30 percent chance
            if chance > 3:
                # creating and sending heart beat messages
                message = "BOOM" + " " + str(seq_num) + " " + str(time.time())
                client_socket.sendto(message.encode('utf-8'), (self.host, self.port))
                print(message)
            # increasing sequence numbers
            seq_num += 1
            time.sleep(0.5)


class Server:
    def __init__(self, port, host):
        self.port = port
        self.host = host

    def run(self):
        server_socket = socket(AF_INET, SOCK_DGRAM)
        server_socket.bind((self.host, self.port))
        # if no heartbeat came for 2 seconds then the client is dead!
        server_socket.settimeout(2)

        server_seq_num = 0

        print("Server is running on", self.host, ":", self.port)
        # listening for heartbeats
        while True:
            try:
                message, addr = server_socket.recvfrom(1024)
                # parsing the payload
                _, seq_num, time_stamp = message.decode().split()
                seq_num = int(seq_num)
                # calculating trip time
                delta = round(time.time() * 1000000) - round(float(time_stamp) * 1000000)

                # deciding packet loss has happen or not
                if server_seq_num == 0:
                    server_seq_num = seq_num
                elif server_seq_num != seq_num:
                    # packet or packets are lost
                    diff = seq_num - server_seq_num
                    if diff == 1:
                        print("Packet number", server_seq_num, " is lost")
                    else:
                        print("Packets with numbers: ",
                              " ".join([str(packet) for packet in range(server_seq_num, seq_num)]), "are lost")
                        # increasing server side sequence number to be the same as the client
                    server_seq_num = seq_num + 1
                    print("Packet number", server_seq_num - 1, "was delivered in", delta, "\u03BCs")
                    continue
                if server_seq_num == seq_num:
                    # no packet loss
                    print("Packet number", server_seq_num, "was delivered in", delta, "\u03BCs")
                server_seq_num += 1

            except timeout:
                # client might not have started yet or is dead
                if server_seq_num == 0:
                    continue
                print("Client has stopped working")


if __name__ == '__main__':
    main()
