# cmpe273-lab3
Lab3 for CMPE 273

Implement sending "Hello World" from client to server via UDP using Twisted Lib.

1. Connected UDP:
Only send and receive datagrams to/from a single address, but this does not in any way imply a connection. Datagrams may still arrive in any order, and the port on the other side may have no one listening. The benefit of the connected UDP socket is that it it may provide notification of undelivered packages.

2. Multicast UDP:
Multicast allows a process to contact multiple hosts with a single packet, without knowing the specific IP address of any of the hosts. This is in contrast to normal, or unicast, UDP, where each datagram has a single IP as its destination. Multicast datagrams are sent to special multicast group addresses (in the IPv4 range 224.0.0.0 to 239.255.255.255), along with a corresponding port. In order to receive multicast datagrams, you must join that specific group address. However, any UDP socket can send to multicast addresses.

REFERENCES: https://twistedmatrix.com/documents/13.2.0/core/howto/udp.html

FILES:

|
| - connected_udp_server.py
| - connected_udp_cleint.py
| - multicast_udp_server.py
| - multicast_udp_cleint.py
|


HOW TO USE:

1. Connected UDP usage:

$ python3.7 connected_udp_server.py (On one machine)


$ python3.7 connected_udp_client.py (On a remote machine, connect to remote server machine IP

1. Multicast UDP usage:

$ python3.7 connected_udp_server.py (On one machine)


$ python3.7 connected_udp_client.py (On a remote machine, join a multicast group IP)

