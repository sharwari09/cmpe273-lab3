from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

PORT = 8000


class HelloWorldServer(DatagramProtocol):

    def datagramReceived(self, datagram, address):
        print("You are in Server now..")
        print("Writing Datagram {} to address {}".format(datagram, address))
        self.transport.write(datagram, address)


if __name__ == '__main__':
    reactor.listenUDP(PORT, HelloWorldServer())
    reactor.run()
