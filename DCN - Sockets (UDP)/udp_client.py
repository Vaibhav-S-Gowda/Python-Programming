import socket

# Create UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1", 5000)

while True:
    msg = input("Enter Message: ")

    client.sendto(msg.encode(), server_address)

    data, addr = client.recvfrom(1024)

    print("Server Reply:", data.decode())