import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "frdge.tk"
        self.port = 2952
        self.addr = (self.server, self.port)
        self.c = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.recieve()
        except socket.error as e:
            print(e)

    def recieve(self):
        count = pickle.loads(self.client.recv(4096))

        d = b''
        while len(d) < count:
            d += self.client.recv(4096)
        return d

    def send(self, data: bytes):
        try:
            self.client.send(pickle.dumps(len(data)))
            self.client.send(data)
            d = self.recieve()
            return d
        except socket.error as e:
            print(e)

    def getC(self):
        return self.c
