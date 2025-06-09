from ..lib import threading, os, sys
from ..config import FORMAT
from ..chat import client
from ..chat.message_handler import handle_incoming, send_loop

def create_group(client):
    group_name = input("Group name to create: ")
    client.send(f'create:{group_name}'.encode(FORMAT))
    os.system('clear')

def enter_group(client, user_name):
    group_name = input("Group name to enter: ")
    client.send(f'create:{group_name}'.encode(FORMAT))

    os.system('clear')

    print(f'welcome to the {group_name}!')
    print("--- Chat ---")
    thread = threading.Thread(target=handle_incoming, args=(client, user_name), daemon=True)
    thread.start()
    send_loop(client)

def list_groups(client):
    client.send('list:'.encode(FORMAT))
    response = client.recv(1024).decode(FORMAT)
    print(f'Groups available:\n{response}')

def leave_group():
    client.send('leave:'.encode(FORMAT))
    sys.exit()