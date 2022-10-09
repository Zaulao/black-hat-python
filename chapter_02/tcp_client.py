import socket

target_host = "localhost"
target_port = 5045

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b"Hello World!\n")

response = client.recv(4096)

print(response.decode())
client.close()

# Test by running in another terminal: nc -lp 5045
# Don't forget to say hello back!
