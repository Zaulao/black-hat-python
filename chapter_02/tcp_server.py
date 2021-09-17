import socket
import threading

IP = 'localhost'
PORT = 5045

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5) # number of simultaneous connections
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        
        # connection received
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        
        # send client into a thread
        client_handler = threading.Thread(target = handle_client, args = (client,))
        client_handler.start()
    
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK\n')

if __name__ == '__main__':
    main()


# Test with: nc -v localhost 5045