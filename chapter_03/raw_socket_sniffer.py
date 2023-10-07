import socket
import os

# local machine IP
HOST = ''

def main():
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))
    
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RVCALL, socket.RCVALL_ON)
    
    print(sniffer.recvfrom(65565))

    if os.name == 'nt':
        # Turn off promiscuous mode
        sniffer.ioctl(socket.SIO_RVCALL, socket.RCVALL_OFF)

if __name__ == '__main__':
    main()