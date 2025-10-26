#Referenced from Chapter_2 Application Layer slides
from socket import*

serverName = '10.245.23.143'#IP Address of Server
serverPort = 12000

try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    sentence = input('Input lowercase sentence:')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print ('From Server:', modifiedSentence.decode())

except Exception as e: #Error if connection not found
    print("Server is not found, please try again")

finally:
    clientSocket.close()
    print("Connection closed")