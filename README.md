# Computer Networking: A Top-Down Approach
## python socket programming assignment

1. In this assignment, you will develop a simple Web server in Python that
is capable of processing only one request. Specifically, your Web server will (i)
create a connection socket when contacted by a client (browser); (ii) receive the
HTTP request from this connection; (iii) parse the request to determine the specific
file being requested;(iv) get the requested file from the server’s file system; (v)
create an HTTP response message consisting of the requested file preceded by
header lines; and (vi) send the response over the TCP connection to the requesting
browser. If a browser requests a file that is not present in your server, your server
should return a “404 Not Found” error message.

2. In the first assignment, instead of using a browser, write your own
HTTP client to test your server. Your client will connect to the server using a TCP
connection, send an HTTP request to the server, and display the server response as
an output. The client not need to display the server response in an HTML format, it
is sufficient for the file just be printed out as a simple text file.
You can assume that the HTTP request sent is a GET method. The client should
take command line arguments specifying the server IP address or host name, the
port at which the server is listening, and the path at which the requested object is
stored at the server. The following is an input command format to run the client.
`client.py server_host server_port filename`

3. In this programming assignment, you will write a client/server ping
program in Python. Your client will send a simple ping message to a server, receive
a corresponding pong message back from the server, and determine the delay
between when the client sent the ping message and received the pong message.
This delay is called the Round Trip Time (RTT). The functionality provided by the
client and server is similar to the functionality provided by standard ping program
available in modern operating systems. However, standard ping programs use the
Internet Control Message Protocol (ICMP) (which we will study in Chapter 5).
Here we will create a nonstandard (but simple!) UDP-based ping program.
Your ping program is to send 10 ping messages to the target server over UDP. For
each message, your client is to determine and print the RTT when the
corresponding pong message is returned. Because UDP is an unreliable protocol, a
packet sent by the client or server may be lost. For this reason, the client cannot
wait indefinitely for a reply to a ping message. You should have the client wait up
to one second for a reply from the server; if no reply is received, the client should
assume that the packet was lost and print a message accordingly.
On the other hand, write the server so that it randomly replies the client. This will
imitate the UDP packet loss.

4. Another similar application to the UDP Ping would be the UDP
Heartbeat. The Heartbeat can be used to check if an application is up and
running and to report one-way packet loss. The client sends a sequence number
and current timestamp in the UDP packet to the server, which is listening for the
Heartbeat (i.e., the UDP packets) of the client. Upon receiving the packets, the
server calculates the time difference and reports any lost packets. If the
Heartbeat packets are missing for some specified period of time, we can assume
that the client application has stopped. Implement the UDP Heartbeat (both
client and server).

