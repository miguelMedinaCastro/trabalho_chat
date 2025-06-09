from ..lib import threading, os
from ..config import FORMAT

def handle_incoming(client, user_name):
    def _receive():
        buffer = ""
        while True:
            try:
                message = client.recv(1024).decode(FORMAT)
                if not message:
                    break

                buffer += message
                while '\n' in buffer:
                    line, buffer = buffer.split('\n', 1)
                    message = line.strip()
                    if message.startswith('msg:'):
                        content = message[4:].strip()
                        if not content.startswith(f'{user_name}:'):
                            print(content)
                    else:
                        print(message)
            except:
                print(f'[Error] receiving message ba tche')
                break

    thread = threading.Thread(target=_receive, daemon=True)
    thread.start()

def send_message(client, message):
    client.send(f'msg: {message}'.encode(FORMAT))

def send_username(client):
    name = input('Username: ').strip()
    client.send(f'name: {name}'.encode(FORMAT))
    return name

def send_loop(client):
    while True:
        message = input()
        if message.lower() in ("sair","/leave"):
            client.send("leave:".encode(FORMAT))
            os.system('clear')
            break
        send_message(client, message)
