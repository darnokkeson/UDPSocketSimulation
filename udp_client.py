from socket import *

# If you want to run server and client on the same machine, use 'localhost'
# If you want to run server on another machine, use its IP address instead
serverName = '127.0.0.1' 
# Indicate a port on the server side (must be the same as the server)
serverPort = 12000
# Create client socket (IPv4, UDP protocol)
clientSocket = socket(AF_INET, SOCK_DGRAM)


message = input('Input lowercase sentence:')

# Send message and server address information to the server
clientSocket.sendto(message.encode(), (serverName, serverPort))
# Receive message from server and server address
# 2048 is the maximum number of bytes the program is willing to read at once
modifiedMessage, serverAdress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())

clientSocket.close()