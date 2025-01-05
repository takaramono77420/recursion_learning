import socket
import os
from faker import Faker

fake = Faker('ja_JP')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = 'localhost'
server_port = 65432

try:
    os.unlink((server_address, server_port))
except:
    pass

print('Starting up on {}'.format(server_address))

sock.bind((server_address, server_port))

sock.listen(1)

while True:
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(16)

            data_str = data.decode('utf-8')

            print('Rreceived :' + data_str)

            if data:
                response = fake.text(max_nb_chars=10).encode('utf-8')
                print(response)
                print(response.decode('utf-8'))

                connection.sendall(response)

            else:
                print('no data from :', client_address)
                break
        
    finally:
        print("Closing current connection")
        connection.close()