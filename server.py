import socket
from _thread import *
import json
from game import Game
import pickle

# Loading variables from JSON
with open("config.json", 'r') as file:
    config = json.load(file)

server = config['server']
port = config['port']

# Creating socket object and binding to local IP & port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    print(str(e))

s.listen()
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0

# Function to handle communication with a connected client
def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p))) # Send the client their player number

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            
            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset()
                    elif data != "get":
                        game.play(p, data)

                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break

    print("Lost connections")

    try:
        del games[gameId]
        print("Closing Game:", gameId)
    except:
        pass

    idCount -= 1

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1) // 2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn))

    # gameID example
    # First player loads in with idCount 1 so (1-1) // 2 = 0 // 2 = 0
    # Second player loads in with idCount 2 so (2-1) // 2 = 1 // 2 = 0
    # Third player loads in with idCount 3 so (3-1) // 2 = 2 // 2 = 1
    # Fourth player loads in with idCount 3 so (4-1) // 2 = 3 // 2 = 1

    # When a player connects and there's an uneven amount of player, a new game is created. When the next person connects that game ready state is set to True