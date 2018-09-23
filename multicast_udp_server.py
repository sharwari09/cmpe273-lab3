from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

TTL = 5
GROUP_IP = "228.0.0.5"
PORT_NO = 9999


class HelloWorldMulticastServer(DatagramProtocol):

    def startProtocol(self):
        self.transport.setTTL(TTL)
        print("Setting TTL..")
        self.transport.joinGroup(GROUP_IP)
        print("Joining Group..")

    def datagramReceived(self, datagram, address):
        print("Datagram {} received from {}".format(datagram,address))
        if datagram == b"Hello World":
            self.transport.write(b"Hello from Server!", address)


reactor.listenMulticast(PORT_NO, HelloWorldMulticastServer(),
                        listenMultiple=True)
reactor.run()

