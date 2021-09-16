import socket

target_host = "localhost"
target_port = 5045

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"Hello World!\n",(target_host, target_port))

data, addr = client.recvfrom(4096)

print(data.decode())
client.close()

# Test by running in another terminal: nc -ulp 5045
# Don't forget to say hello back!