from __future__ import print_function
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class HelloWorldClient(DatagramProtocol):
    def startProtocol(self):
        # Remote Machine IP "10.0.0.221"
        HOST_IP = input("Enter Server Host IP to connect to: ")
        PORT_NO = int(input("Enter Server Port number: "))
        self.transport.connect(HOST_IP, PORT_NO)
        print(("Send to host %s port %d" % (HOST_IP, PORT_NO)))
        self.transport.write(b"Hello World")

    def datagramReceived(self, data, addr):
        print("received %r from %s" % (data, addr))

    def connectionRefused(self):
        print("No one listening")


reactor.listenUDP(0, HelloWorldClient())
reactor.run()
