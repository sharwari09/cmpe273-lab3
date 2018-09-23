from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

TTL = 5

GROUP_IP = input("Enter Group IP to join to : ")
PORT_NO = int(input("Enter Server Port number: "))

class HelloWorldMulticastServer(DatagramProtocol):

    def startProtocol(self):
        self.transport.setTTL(TTL)
        print("Setting TTL..")

        self.transport.joinGroup(GROUP_IP)
        print("Joining Group..")

    def datagramReceived(self, datagram, address):
        print("Datagram {} received from {}".format(datagram,address))
        if datagram == b"Hello from Client!":
            self.transport.write(b"Hello from Server!", address)


reactor.listenMulticast(PORT_NO,
                        HelloWorldMulticastServer(),
                        listenMultiple=True)
reactor.run()

