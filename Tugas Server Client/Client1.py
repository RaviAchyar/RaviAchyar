import socket
import threading

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5002
separator_token = "<SEP>"

def listen_for_messages(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg:
                print("\n" + msg)
            else:
                break
        except Exception as e:
            print(f"[!] Error menerima pesan: {e}")
            break
    client_socket.close()

username = input("Masukkan username: ")

def send_messages(client_socket):
    while True:
        try:
            msg = input("> ")
            if msg.lower() == 'exit':
                break
            full_msg = f"{username}{separator_token}{msg}"
            client_socket.send(full_msg.encode())
        except (BrokenPipeError, ConnectionResetError):
            print("[!] Koneksi ke server terputus.")
            break
        except Exception as e:
            print(f"[!] Error mengirim pesan: {e}")
            break
    client_socket.close()

if __name__ == "__main__":
    try:
        client_socket = socket.socket()
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print(f"[*] Terhubung ke server di {SERVER_HOST}:{SERVER_PORT}")

        threading.Thread(target=listen_for_messages, args=(client_socket,), daemon=True).start()

        send_messages(client_socket)
    except Exception as e:
        print(f"[!] Gagal terhubung ke server: {e}")
