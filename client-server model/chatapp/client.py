import socket

# UNIXドメインソケットとデータグラム（非接続）ソケットを作成します
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# サーバのアドレスを定義します。
# サーバはこのアドレスでメッセージを待ち受けます
server_address = ('localhost', 9000)

# サーバに送信するメッセージを定義します
user_address = input('address: ')
user_port = input('port :')

sock.bind((user_address, int(user_port)))
#sock.settimeout(50)

username = input('username: ')
username = username.encode('utf-8')
message = input('message: ')
message = message.encode('utf-8')

# このクライアントのアドレスをソケットに紐付けます。
# これはUNIXドメインソケットの場合に限ります。
# このアドレスは、サーバによって送信元アドレスとして受け取られます。


try:
    # サーバにメッセージを送信します
    sent_username = sock.sendto(username, server_address)
    sent = sock.sendto(message, server_address)

    while True:

        # サーバからの応答を待ち受けます
        print('waiting to receive')
        # 最大4096バイトのデータを受け取ります
        data, server = sock.recvfrom(4096)

        # サーバから受け取ったメッセージを表示します
        print(data.decode('utf-8'))

except socket.timeout:
    print("Timeout: No data received.")

