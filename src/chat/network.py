from ..lib import socket
from ..config import PORT

def create_client():
    server_ip = input("type IP server: ").strip()
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((server_ip, PORT))
    except ConnectionRefusedError:
        print(f'[Error] not possible to connect a {server_ip}: {PORT}')
        exit(1)

    # client.connect(ADDR)
    return client