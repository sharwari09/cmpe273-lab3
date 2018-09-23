# cmpe273-lab3
Lab3 for CMPE 273

Implement sending "Hello World" from client to server via UDP using Twisted Lib.

1. **_Connected UDP_**:
Only send and receive datagrams to/from a single address, but this does not in any way imply a connection. Datagrams may still arrive in any order, and the port on the other side may have no one listening. The benefit of the connected UDP socket is that it it may provide notification of undelivered packages.

2. **_Multicast UDP_**:
Multicast allows a process to contact multiple hosts with a single packet, without knowing the specific IP address of any of the hosts. This is in contrast to normal, or unicast, UDP, where each datagram has a single IP as its destination. Multicast datagrams are sent to special multicast group addresses (in the IPv4 range 224.0.0.0 to 239.255.255.255), along with a corresponding port. In order to receive multicast datagrams, you must join that specific group address. However, any UDP socket can send to multicast addresses.

REFERENCES: https://twistedmatrix.com/documents/13.2.0/core/howto/udp.html

FILES:

|</br>
| - connected_udp_server.py</br>
| - connected_udp_cleint.py</br>
| - multicast_udp_server.py</br>
| - multicast_udp_cleint.py</br>
|


HOW TO USE:

1. _Connected UDP usage_:

$ **python3.7 connected_udp_server.py**

Sharwaris-MacBook-Pro:cmpe273-lab3 sharwariphadnis$ python3.7 connected_udp_server.py</br>
You are in Server now..</br>
Writing Datagram b'Hello World' to address ('10.0.0.221', 49327)</br>


$ **python3.7 connected_udp_client.py (On a remote machine)**

Sharwaris-MacBook-Pro:cmpe273-lab3 sharwariphadnis$ python3.7 connected_udp_client.py </br>
Enter Server Host IP to connect to: 10.0.0.221</br>
Enter Server Port number: 8000</br>
Send to host 10.0.0.221 port 8000</br>
received b'Hello World' from ('10.0.0.221', 8000)</br>



1. _Multicast UDP usage_:

$ **python3.7 multicast_udp_server.py (On one machine)**

Sharwaris-MacBook-Pro:cmpe273-lab3 sharwariphadnis$ python3.7 multicast_udp_server.py 
Enter Group IP to join to : 228.0.0.5</br>
Enter Server Port number: 9999</br>
Setting TTL..</br>
Joining Group..</br>
Datagram b'Hello World' received from ('10.0.0.27', 9999)</br>
Datagram b'Hello from Server!' received from ('10.0.0.27', 9999)</br>


$ **python3.7 multicast_udp_client.py (On a remote machine, join a multicast group IP)**
</br>
Sharwaris-MacBook-Pro:cmpe273-lab3 sharwariphadnis$ python3.7 multicast_udp_client.py</br>
Enter Group IP to join to : 228.0.0.5</br>
Enter Server Port number: 9999</br>
Datagram b'Hello World' received from ('10.0.0.27', 9999)
