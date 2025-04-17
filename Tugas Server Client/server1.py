import socket
from threading import Thread

SERVER_HOST = "192.168.1.1"
SERVER_PORT = 5002
separator_token = "<SEP>"

client_sockets = set()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

def listen_for_client(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"[!] Disconnect: {e}")
            client_sockets.remove(cs)
            cs.close()
            break
        else:
            msg = msg.replace(separator_token, ": ")
            for client_socket in client_sockets:
                if client_socket in (client_sockets):
                    try:
                        client_socket.send(msg.encode())
                    except:
                        client_sockets.remove(client_socket)

while True:
    client_socket, client_address = s.accept()
    print(f"(+) {client_address} connected.")
    client_socket.add(client_socket)
    t = Thread(target=listen_for_client, args=(client_socket,))
    t.daemon = True
    t.start()

