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
        # set 1 second time out

        print("Client is running on", self.host, ":", self.port)
        seq_num = 0
        while True:
            chance = random.randint(0, 10)
            if chance > 3:
                message = "BOOM" + " " + str(seq_num) + " " + str(time.time())
                client_socket.sendto(message.encode('utf-8'), (self.host, self.port))
                print(message)

            seq_num += 1
            time.sleep(0.5)


class Server:
    def __init__(self, port, host):
        self.port = port
        self.host = host

    def run(self):
        server_socket = socket(AF_INET, SOCK_DGRAM)
        server_socket.bind((self.host, self.port))
        server_socket.settimeout(2)

        server_seq_num = 0

        print("Server is running on", self.host, ":", self.port)
        while True:
            try:
                message, addr = server_socket.recvfrom(1024)
                _, seq_num, time_stamp = message.decode().split()
                seq_num = int(seq_num)
                delta = round(time.time() * 1000000) - round(float(time_stamp) * 1000000)
                if server_seq_num == 0:
                    server_seq_num = seq_num
                elif server_seq_num != seq_num:
                    diff = seq_num - server_seq_num
                    if diff == 1:
                        print("Packet number", server_seq_num, " is lost")
                    else:
                        print("Packets with numbers: ",
                              " ".join([str(packet) for packet in range(server_seq_num, seq_num)]), "are lost")
                    server_seq_num = seq_num + 1
                    print("Packet number", server_seq_num - 1, "was delivered in", delta, "\u03BCs")
                    continue
                if server_seq_num == seq_num:
                    print("Packet number", server_seq_num, "was delivered in", delta, "\u03BCs")
                server_seq_num += 1

            except timeout:
                if server_seq_num == 0:
                    continue
                print("Client has stopped working")


if __name__ == '__main__':
    main()
