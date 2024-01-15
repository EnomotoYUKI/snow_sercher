import socket
import datetime
import os
from dotenv import load_dotenv


class dataReceive:
    def __init__(self):
        load_dotenv()
        
        
    def receiveData(self):
        ip = "0.0.0.0"
        port = 12345
        output_list = []
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((ip, port))
            s.listen(1)
            while True:
                conn, addr = s.accept()
                with conn:
                    dt_now = datetime.datetime.now()
                    fname = "./Cloud/strage/" + dt_now.strftime('%Y%m%d%H%M%S') + "_received.csv"
                    with open(fname, mode="ab") as f:
                        while True:
                            data = conn.recv(1024)
                            if not data:
                                break
                            f.write(data)
                            conn.sendall(b'Received done')
                return fname
if __name__ == '__main__':
	sd = dataReceive()
	sd.receiveData()
