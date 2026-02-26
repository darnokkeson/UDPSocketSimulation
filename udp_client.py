from socket import *

serverName = '172.20.10.5'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentence:')

clientSocket.sendto('answer from phone server', (serverName, serverPort))
modifiedMessage, serverAdress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())

clientSocket.close()