import socket
import os
import datetime
import asyncio
import secrets

class User:

    current_id = 0

    def __init__(self, name, last_message_time, address, room_host):
        self.id = User.create_id()
        self.username = name
        self.time = last_message_time
        self.address = address
        self.error = 0
        self.room_host = room_host
    
    @staticmethod
    def create_id():
        User.current_id += 1
        return User.current_id
    
    def count_error(self):
        self.error += 1


class ChatRoom:

    current_id = 0

    def __init__(self, room_name):
        self.id = ChatRoom.create_id()
        self.room_name = room_name
        self.users = {}

    def add_user(self, new_user, user_token):
        self.users[user_token] = new_user

    def delete_user(self, target_user):
        self.users.pop(target_user.id)

    def time_out(self):
        for user in self.users.values():
            if (datetime.datetime.now() - user.time).total_seconds() > 60:
                self.delete_user(user)
    
    @staticmethod
    def create_token():
        return secrets.token_hex()
    
    @staticmethod
    def create_id():
        User.current_id += 1
        return User.current_id

success_code = 202

async def user_reception(chat_room_hashmap):

    user_reception_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = 'localhost'
    server_port_chat_room = 8000

    user_reception_sock.bind((server_address, server_port_chat_room))

    user_reception_sock.listen(1)

    try:

        while True:

            connection, client_address = user_reception_sock.accept()

            #ヘッダー受信
            header = connection.recv(32)
            room_name_size = int.from_bytes(header[:1], 'big')
            operation = int.from_bytes(header[1:2], 'big')
            state = int.from_bytes(header[2:3], 'big')
            operation_payload_size = int.from_bytes(header[3:32], 'big')

            #ボディー受信
            room_name = connection.recv(room_name_size)
            operation_payload = connection.recv(operation_payload_size)

            room_name = room_name.decode('utf-8')
            operation_payload = operation_payload.decode('utf-8')

            if operation == 1:
                #サーバの初期化
                user = User(operation_payload, datetime.datetime.now(), client_address, True)
                chat_room = ChatRoom(room_name)
                user_token = ChatRoom.create_token(chat_room.chat_room_id)
                chat_room.add_user(user, user_token)
                chat_room_hashmap[chat_room.name] = chat_room

                print(user.address)

                #リクエストの応答
                connection.send(success_code.to_byte(2, 'big'))

                #リクエストの完了
                connection.send(user_token.encode('utf-8') + chat_room.id.to_bytes(2, 'big'))
            
            elif operation == 2:
                user = User(operation_payload, datetime.datetime.now(), client_address, False)
                user_token = ChatRoom.create_token()
                chat_room_hashmap[room_name].add_user(user, user_token)

                #リクエストの応答
                connection.send(success_code.to_byte(2, 'big'))

                #リクエストの完了
                connection.send(user_token.encode('utf-8') + chat_room.id.to_bytes(2, 'big'))
        
    except Exception as e:
        print('Error: ' + str(e))

    finally:
        print("Closing current connection")
        connection.close()

#async def send_messages():


#ユーザーの受付

chat_room_list = {}

asyncio.run(user_reception(chat_room_list))

#メッセージの送受信

# socket.socket関数を使用して、新しいソケットを作成します。
# AF_UNIXはUNIXドメインソケットを表し、SOCK_DGRAMはデータグラムソケットを表します。
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# サーバが接続を待ち受けるUNIXドメインソケットのパスを指定します。
server_address = 'localhost'
server_port = 8500

# ソケットが起動していることを表示します。
print('starting up on {} port {}'.format(server_address, server_port))

# sockオブジェクトのbindメソッドを使って、ソケットを特定のアドレスに関連付けます。
sock.bind((server_address, server_port))

# ソケットはデータの受信を永遠に待ち続けます。
while True:
    print('\nwaiting to receive message')#

    # ソケットからの認証データを受信します。
    header, user_address = sock.recvfrom(2)

    room_name_size = int.from_bytes(header[:1], 'big')
    token_size = int.from_bytes(header[1:2], 'big')

    body, user_address = sock.recvfrom(4096)

    room_name = body[:room_name_size].decode('utf-8')
    token = body[room_name_size:token_size].decode('utf-8')
    message = body[token_size:].decode('utf-8')

    #ユーザー認証
    chat_room = chat_room_list[room_name]
    user = None
    authenticate_error_code = 401
    
    if token in chat_room.users.keys():
        user = chat_room.users[token]
        if user_address == user.address:
            print(user.username + ': Authenticated.')
        else:
            print(user.username + ' failed to authenticate')
            
            sock.sendto(authenticate_error_code.to_bytes(2, 'big'), user_address)
            continue
    else:
        print(user.username + ' failed to authenticate')
        sock.sendto(authenticate_error_code.to_byte(2, 'big'), user_address)
        continue

    try:

        message, address = sock.recvfrom(4096)

        chat_room.time_out()

        for user in chat_room.users.values():
            sock.sendto(message, user.address)
        
        # 受信したデータのバイト数と送信元のアドレスを表示します。
        message = message.decode(encoding='utf-8')
        print('received message [{}] from [{}]'.format(message, user.username))
        
    except:
       user.count_error()
