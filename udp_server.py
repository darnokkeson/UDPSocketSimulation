from socket import *

# Choose a port (must be unique to prevent conflicts with other programs)
serverPort = 12000
# create socket(IPv4, UDP protocol)
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Bind - assign IP and port for listening
# '' means listen for all IPs
# serverPort listens on port 12000 
serverSocket.bind(('', serverPort))

print ("The server is ready to receive")

while True:
    # Receive message from client with client address (IP and port)
    # 2048 is the maximum number of bytes the program is willing to read at once
    message, clientAdress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()

    # Send message back to client
    serverSocket.sendto(modifiedMessage.encode(), clientAdress)
