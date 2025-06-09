from ..lib import socket, threading
from ..config import HOST_SERVER, PORT
from .client_handler import handle_clients

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST_SERVER, PORT))
    server.listen()

    print(f"[Listening] in {HOST_SERVER}: {PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clients, args=(conn, addr))
        thread.start()
        print(f'[Active Connections] {threading.active_count() - 1}')