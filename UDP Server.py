#Referenced/Adapted from Chapter 2 Slides
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    decodedMessage = message.decode().strip()
    print(f"Received from {clientAddress}: {decodedMessage}")

    # Check if client wants to quit
    if decodedMessage.lower() in ['quit', 'exit']:
        serverSocket.sendto("Connection closed by server.".encode(), clientAddress)
        print(f"Client {clientAddress} requested to end session.")
        continue  # stays running for other clients;

    # Otherwise, send uppercase version back
    modifiedMessage = decodedMessage.upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)