from ..lib import time, threading, os
from ..config import FORMAT

groups = {}

connections = []

def group_send_loop(info_conn):
    while True:
        group = info_conn['group']
        if not group:
            break

        messages = groups[group]['messages']
        
        for i in range(info_conn['last'], len(messages)):
            try:
                info_conn['conn'].send(f'msg: {messages[i]}\n'.encode(FORMAT))
                info_conn['last'] = i + 1
                time.sleep(0.2)
            except:
                continue

        time.sleep(0.5)

def handle_clients(conn, addr):
    print(f'[New Connection] {addr}')
    name = None

    info_conn = {
        'conn': conn,
        'addr': addr,
        'name': '',
        'last': 0,
        'group': None,
        'loop_started': False
    }

    while True:
        try:
            data = conn.recv(1024).decode(FORMAT)
            if not data:
                break
            if data.startswith('name:'):
                _, name = data.split(':', 1)
                info_conn['name'] = name.strip()
                connections.append(info_conn)
                print(f'[User Connected] {info_conn["name"]}')
           
            elif data.startswith('create:'):
                _, group_name = data.split(':', 1)
                if group_name not in groups:
                    groups[group_name] = {
                        'members': [],
                        'messages': []
                    }
                info_conn['group'] = group_name
                
                groups[group_name]['members'].append(info_conn)

                if not info_conn['loop_started']:
                    info_conn['loop_started'] = True
                    threading.Thread(target=group_send_loop, args=(info_conn, ), daemon=True).start()

            elif data.startswith('join:'):
                _, group_name = data.split(':', 1)
                group_name = group_name.strip()
                if group_name in groups:
                    info_conn['group'] = group_name

                    groups[group_name]['members'].append(info_conn)

                    for message in groups[group_name]['messages']:
                        try:
                            conn.send(f'msg: {message}\n'.encode(FORMAT))
                            time.sleep(0.2)
                        except:    
                            print('[Error] sending history')

                    info_conn['last'] = len(groups[group_name]['messages'])

                    if not info_conn['loop_started']:
                        info_conn['loop_started'] = True
                        threading.Thread(target=group_send_loop, args=(info_conn,), daemon=True).start()

                    conn.send(f'enter in group {group_name}'.encode(FORMAT))
                else:
                    conn.send(f'Group {group_name} does not exists'.encode(FORMAT))

            elif data.startswith('list:'):
                if not groups:
                    conn.send('No groups available.\n'.encode(FORMAT))
                    os.system('clear')
                else:
                    response = 'Groups:\n'
                    for group_name in groups:
                        response += f'- {group_name}\n'
                    conn.send(response.encode(FORMAT))
            
            elif data.startswith('leave:'):
                group = info_conn['group']
                if group and info_conn in groups[group]['members']:
                    groups[group]['members'].remove(info_conn)
                    info_conn['group'] = None
                    info_conn['loop_started'] = False

            elif data.startswith('msg:') and info_conn['group']:
                _, content = data.split(':', 1)
                group = info_conn['group']
                message = f'{info_conn["name"]}: {content.strip()}'

                groups[group]['messages'].append(message)

                print(f'[Broadcast] {message} to group: {group}')

        except ConnectionResetError:
            print(f'[Disconnected] {addr}')
