from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastPingClient(DatagramProtocol):

    def startProtocol(self):
        self.transport.joinGroup("202.0.0.2")
        self.transport.write(b'Hello World', ("202.0.0.2", 9999))

    def datagramReceived(self, datagram, address):
        print("Datagram {} received from {}".format(datagram,address))

reactor.listenMulticast(9999, MulticastPingClient(), listenMultiple=True)
reactor.run()
