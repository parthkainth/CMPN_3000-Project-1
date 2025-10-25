#Referenced from Chapter_2 Application Layer slides
from socket import*
try:
    serverName = '10.245.23.143'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    sentence = input('Input lowercase sentence:')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print ('From Server:', modifiedSentence.decode())

except:
    print("Server is not found")
clientSocket.close()