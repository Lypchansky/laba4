# Завдання 1-1а
import socket
import sys

def run_server():
    HOST = '127.0.0.1'
    PORT = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        print(f"Підключення до сервера {HOST}:{PORT}.")
        conn, addr = server_socket.accept()
        with conn:
            print(f"З'єднано за допомогою {addr}.")

            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Отримано: {data.decode('utf-8')}.")
                conn.sendall(data)

def run_client():
    HOST = '127.0.0.1'
    PORT = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        message = input("Повідомлення для відправки на сервер: ")
        client_socket.sendall(message.encode('utf-8'))
        data = client_socket.recv(1024)
        print(f"Отримано з сервера: {data.decode('utf-8')}")

if __name__ == "__main__":
    mode = input("Оберіть режим (s-server/c-client): ").strip().lower()

    if mode == "s":
        run_server()
    elif mode == "c":
        run_client()
    else:
        print("Неіснуючий режим.")
