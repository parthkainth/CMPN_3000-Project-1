#Referenced/Adapted from Chapter 2 Application Layer slides
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f'Connected to {addr}')

    while True:
        sentence = connectionSocket.recv(1024).decode()
        if not sentence:
            break

        print(f"Received from {addr}: {sentence}")

        if sentence.lower() in ['quit', 'exit']:
            print(f"Connection closed by client {addr}")
            connectionSocket.send("Connection closed by server.".encode())
            break

        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())

    connectionSocket.close()
    print(f"Connection with {addr} ended.\n")