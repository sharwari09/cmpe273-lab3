from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

GROUP_IP = "228.0.0.5"
PORT_NO = 9999


class HelloWorldMulticastClient(DatagramProtocol):

    def startProtocol(self):
        # Taking Group IP in the range of 224.0.0.0 to 239.255.255.255
        self.transport.joinGroup(GROUP_IP)
        self.transport.write(b'Hello World', (GROUP_IP, PORT_NO))

    def datagramReceived(self, datagram, address):
        print("Datagram {} received from {}".format(datagram,address))


reactor.listenMulticast(PORT_NO, HelloWorldMulticastClient(),
                        listenMultiple=True)
reactor.run()
