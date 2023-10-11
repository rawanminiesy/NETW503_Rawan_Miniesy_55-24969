import socket
import select
import sys

def capitalize_message(message):
    return message.upper()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port=12346
    server_socket.bind(('localhost', port))
    server_socket.listen(1)

    print('Server is listening on port 12346...')

    while True:
        client_socket, client_address = server_socket.accept()
        print('Connected to', client_address)

        while True:
            info = client_socket.recv(1024).decode('utf-8')
            if not info:
                break

            capitalized_info = capitalize_message(info)
            client_socket.send(capitalized_info.encode('utf-8'))
            print('Message sent:', capitalized_info)

        client_socket.close()

start_server()