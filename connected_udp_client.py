from __future__ import print_function
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class HelloWorldClient(DatagramProtocol):
    def startProtocol(self):
        # Remote Machine IP "10.0.0.221"
        host = "10.0.0.221"
        port = 8000
        self.transport.connect(host, port)
        print(("Send to host %s port %d" % (host, port)))
        self.transport.write(b"Hello World")

    def datagramReceived(self, data, addr):
        print("received %r from %s" % (data, addr))

    def connectionRefused(self):
        print("No one listening")


reactor.listenUDP(0, HelloWorldClient())
reactor.run()
