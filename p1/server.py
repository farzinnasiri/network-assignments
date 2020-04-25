from socket import *


def serve():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('localhost', 80))
    server_socket.listen(1)

    print("Server Running on port 80")
    while True:
        connection_socket, address = server_socket.accept()

        try:
            request = connection_socket.recv(1024)
            file_name = request.split()[1][1:]
            output = open(file_name).read()
            # http header
            connection_socket.send("HTTP/1.1 200 OK\r\n\r\n".encode('utf-8'))
            # payload
            connection_socket.send(output.encode('utf-8'))
        except IOError:
            # not found
            output = open("404.html").read()
            connection_socket.send("\nHTTP/1.1 404 Not Found\n\n".encode('utf-8'))
            connection_socket.send(output.encode('utf-8'))


if __name__ == '__main__':
    serve()
