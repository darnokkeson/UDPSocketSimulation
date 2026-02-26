# UDPSocketSimulation
A simple UDP (User Datagram Protocol) client-server communication program that converts messages to uppercase.

## Overview

This project demonstrates basic UDP socket programming with a server that listens for incoming messages and converts them to uppercase, and a client that sends messages to the server and receives the modified response.

## Files

- `udp_server.py` - The server script that listens for incoming messages
- `udp_client.py` - The client script that sends messages to the server

## Usage

### Running on the Same Machine

1. **Start the server:**
   ```
   python udp_server.py
   ```
   The server will print: "The server is ready to receive"

2. **In another terminal, run the client:**
   ```
   python udp_client.py
   ```
   - Enter a lowercase message when prompted
   - The server will convert it to uppercase and send it back
   - The modified message will be displayed

### Running on Different Machines in the Same Network

These scripts can be run on different machines connected to the same network:

1. **On the Server Machine:**
   - Run `python udp_server.py`
   - Note the server's IP address (e.g., 192.168.1.100)

2. **On the Client Machine:**
   - Edit `udp_client.py` and change the `serverName` variable to the server machine's IP address
   - Run `python udp_client.py`
   - Enter your message when prompted

## Configuration

- **Server Port:** Default is `12000`. Can be changed in both scripts if needed (must match on both client and server)
- **Server Address:** In `udp_client.py`, set `serverName` to:
  - `'localhost'` or `'127.0.0.1'` to run on the same machine
  - The server's IP address to run on different machines