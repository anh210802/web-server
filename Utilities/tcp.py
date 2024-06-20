import socket
import threading


class TCPClient:
    def __init__(self, _host, _port):
        self.host = _host
        self.port = _port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lock = threading.Lock()
        self.data_received = ""

    def on_connect(self):
        try:
            self.client.connect((self.host, self.port))
            print(f"Connected to server is successful :)")
            self.handle_data()
        except socket.error:
            print(f"Connected to server is fail :(")

    def handle_data(self):
        try:
            while True:
                self.data_received = self.client.recv(1024).decode()
                if not self.data_received:
                    break


        except Exception as e:
            pass

