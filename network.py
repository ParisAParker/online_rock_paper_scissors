import socket
import pickle
import json

# Load in config.json
with open('config.json', 'r') as file:
    config = json.load(file)

# Load in variables from config.json
server = config['server']
port = config['port']

# Create class that's responsible for connecting to the server
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data)) # Send a string
            return pickle.loads(self.client.recv(2048)) # Load an object
        except socket.error as e:
            print(e)