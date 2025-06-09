from ..lib import socket
from ..config import ADDR

def create_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client