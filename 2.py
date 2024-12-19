import socket

def run_server():
    HOST = '127.0.0.1'
    PORT = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print(f"Підключення до сервера {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            print(f"З'єднано за допомогою {addr}.")

            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Отримано від {addr}: {data.decode('utf-8')}.")
                    conn.sendall(data)

if __name__ == "__main__":
    run_server()
