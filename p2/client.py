from socket import *
import sys


def main(host_name, port_num, filename):
    try:
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((host_name, port_num))

        # creating http request
        request = "GET /{filename} HTTP/1.1\r\n" \
                  "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n" \
                  "Accept-Language: en-us\r\n" \
                  "Host: {host}\r\n" \
                  "\r\n".format(filename=filename, host=host_name)

        client_socket.send(request.encode("utf-8"))

    except IOError:
        sys.exit(1)

    response_message = client_socket.recv(1024)
    # listening for response messages
    while response_message:
        print(response_message)
        response_message = client_socket.recv(1024)
    client_socket.close()


if __name__ == '__main__':
    # getting command line arguments
    host = sys.argv[1]
    port = int(sys.argv[2])
    file = sys.argv[3]

    main(host, port, file)

# sample input1: python client.py localhost 80 index.html
# sample input2: python client.py localhost 80 404.html
