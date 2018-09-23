from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastPingPong(DatagramProtocol):

    def startProtocol(self):
        """
        Called after protocol has started listening.
        """
        self.transport.setTTL(5)
        print("Setting TTL..")
        self.transport.joinGroup("228.0.0.5")
        print("Joining Group..")

    def datagramReceived(self, datagram, address):
        print("Datagram {} received from {}".format(datagram,address))
        if datagram == b"Hello World":
            self.transport.write(b"Hello from Server!", address)


reactor.listenMulticast(9999, MulticastPingPong(),
                        listenMultiple=True)
reactor.run()

