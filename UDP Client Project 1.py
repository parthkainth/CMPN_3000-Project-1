#Referenced from Chapter_2 Application Layer slides
from socket import*

serverName = '10.245.23.143'#IP Address of Server
serverPort = 12000

try: #UDP Socket Creation
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(30)
    message = input('Input lowercase sentence')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())  

except timeout: 
    print("Request has timed out please retry") 

finally:
    clientSocket.close()
    print("Program completed")
