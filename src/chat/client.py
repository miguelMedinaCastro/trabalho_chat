from .network import create_client
from .message_handler import handle_incoming, send_username, send_loop
from ..features import interface

client = create_client()

def run_client():
    name = send_username(client)
    interface(client, name)
    handle_incoming(client, name)
    send_loop(client)

