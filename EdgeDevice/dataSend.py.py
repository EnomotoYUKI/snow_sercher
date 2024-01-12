import socket
import os
from dotenv import load_dotenv


class dataSend:
    def __init__(self, csv_path:str):
        # .envファイルの内容を読み込みます
        load_dotenv()
        self.csv_path = csv_path

def sendData(self):
	ip_address = os.environ.get("CLOUD_HOSTNAME")
	port = os.environ.get("CLOUD_PORT")
	buffer_size = 1024
	# ソケットの作成
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect((ip_address, port))

	# データを受信してファイルに保存
	with open(self.csv_path, 'wb') as f:
		data = client_socket.recv(buffer_size)
		f.write(data)

	# ソケットを閉じる
	client_socket.close()

