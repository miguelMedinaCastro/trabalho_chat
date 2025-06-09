from .lib import sys

def server_init():
    from .server.network import start_server
    start_server()

def start_client():
    from .chat.client import run_client
    run_client()
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('use: python3 -m src.main [serve|client]')
        sys.exit(1)
    
    mode = sys.argv[1].lower().strip()

    if mode == 'server':
        server_init()
    elif mode == 'client':
        start_client()
    else:
        print("invalid mode. Use 'server ou 'client'")