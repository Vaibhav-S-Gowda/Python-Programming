import socket

# Create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind IP and Port
server.bind(("127.0.0.1", 5000))

print("UDP Server Waiting...\n")

while True:
    # Receive message
    data, addr = server.recvfrom(1024)

    message = data.decode()

    print("Client Message:", message)

    # Convert to uppercase
    upper_message = message.upper()

    # Send uppercase message back
    server.sendto(upper_message.encode(), addr)