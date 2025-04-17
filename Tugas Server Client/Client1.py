import socket
import threading

SERVER_HOST = "192.168.1.1"
SERVER_PORT = 5002
separator_token = "<SEP>"

def listen_for_messages(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg:
                print(msg) 
            else:
                break 
        except Exception as e:
            print(f"[!] Error: {e}")
            break

    client_socket.close()

def send_messages(client_socket):
    while True:
        msg = input()  
        if msg.lower() == 'exit': 
            break
        client_socket.send(msg.encode())

    client_socket.close()

if __name__ == "__main__":
    client_socket = socket.socket()
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"[*] Connected to the server at {SERVER_HOST}:{SERVER_PORT}")

    threading.Thread(target=listen_for_messages, args=(client_socket,), daemon=True).start()

    send_messages(client_socket)