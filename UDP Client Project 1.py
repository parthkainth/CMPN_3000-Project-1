#Referenced from Chapter_2 Application Layer slides
from socket import*

try: #Execute Code
    serverName = '10.245.23.143'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(30)
    message = input('Input lowercase sentence')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())  

except: #If packets cannot be received error
    print("Error please retry") 

clientSocket.close()
