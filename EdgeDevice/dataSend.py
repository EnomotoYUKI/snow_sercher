import socket
import os
from dotenv import load_dotenv


class dataSend:
	def __init__(self, csv_path:str):
		# .envファイルの内容を読み込みます
		load_dotenv()
		self.csv_path = csv_path
		
	def sendData(self):
		ip = os.environ.get("CLOUD_HOSTNAME")
		port = int(os.environ.get("CLOUD_PORT"))
		buffer_size = 1024

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.connect((ip, port))
			try:
				with open(self.csv_path, mode='rb') as f:
					for line in f:
						s.sendall(line)
						data = s.recv(1024)
					print(repr(data.decode()))
			except:
				pass


if __name__ == '__main__':
	sd = dataSend("EdgeDevice/strage/test.csv")
	sd.sendData()
