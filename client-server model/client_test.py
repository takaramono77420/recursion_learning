import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = 'localhost'
server_port = 65432

print('connectting to {}'.format(server_address))

try:
    sock.connect((server_address, server_port))
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    message = input('me: ')
    sock.sendall(message.encode('utf-8'))

    sock.settimeout(2)

    try:
        while True:
            data = sock.recv(32) #.decode('utf-8')

            if data:
                print('Server response: ' + data)
            else:
                break
    
    except(TimeoutError):
        print('Socket timeout, ending listening for server messages')

finally:
    print('closing socket')
    sock.close()
