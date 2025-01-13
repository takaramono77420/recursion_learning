import socket
import sys
import os

# protocol_header()という関数は、サーバに送信されるファイルのヘッダ情報をフォーマットするために使用されます。このヘッダは、ファイル名の長さ（バイト）、JSONデータの長さ（バイト）、データの長さ（バイト）の3つの値で構成されます。これらの値は、to_bytes()メソッドを用いてバイナリに変換され、1つの64ビットバイナリに結合されます。
def entry_protocol_header(room_name_size, operation, state, operation_payload_size):
    return room_name_size.to_bytes(1, "big") + operation.to_bytes(1,"big") + state.to_bytes(1,"big") + operation_payload_size.to_bytes(1,"big")

def message_protocol_header(room_name_size, token_size):
    return room_name_size.to_bytes(1, 'big') + token_size.to_bytes(1, 'big')

def message_protocol_body(room_name, token, message):
    return room_name.encode('utf-8') + token.encode('utf-8') + message.encode('utf-8')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# (entry)サーバが待ち受けているポートにソケットを接続します
entry_server_address = 'localhost'
entry_server_port = 8000

# (message)サーバが待ち受けているポートにソケットを接続します
message_server_address = 'localhost'
message_server_port = 8500

# クライアント側
client_address = 'localhost'
client_port = 9000

sock.bind((client_address, client_port))

print('connecting to {}'.format(entry_server_address, entry_server_port))

# エントリー処理
try:
    # 接続後、サーバとクライアントが相互に読み書きができるようになります
    sock.connect((entry_server_address, entry_server_port))
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    # ファイルを送信する場合は、テキストファイルで2GB以下に制限してください
    user_name = input('your name: ')
    operation = input('1:create room, 2:connect room :')
    room_name = input('room name: ')

    # ファイル名からビット数
    user_name_bits = user_name.encode('utf-8')
    room_name_bits = room_name.encode('utf-8')

    # protocol_header()関数を用いてヘッダ情報を作成し、ヘッダとファイル名をサーバに送信します。
    header = entry_protocol_header(len(room_name_bits), int(operation), 202, len(user_name_bits))

    # ヘッダの送信
    sock.send(header)

    # ルーム名とユーザー名を送信
    sock.send(room_name_bits)
    sock.send(user_name_bits)

    # ステータスを受信
    status = sock.recv(32).decode('utf-8')
    print('status : ' + status)

    user_token = sock.recv(34)
    
finally:
    sock.close()

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    
    user_token_bits = user_token.encode('utf-8')

    while True:

        message = input('message : ')

        header = message_protocol_header(len(room_name_bits), len(user_name_bits))
        sock.sendto(header, (message_server_address, message_server_port))

        #status = sock.recv(2)

        body = message_protocol_body(room_name, user_token, message)
        sock.sendto(body, (message_server_address, message_server_port))

        



    



    



finally:
    print('closing socket')
    sock.close()

# メッセージ送信