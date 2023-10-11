import socket
import select
import sys

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port=12346
    client_socket.connect(('localhost', port))

    while True:
        message = input('Enter a message or "close socket" to quit: ')

        if message.lower() == 'close socket':
            break

        client_socket.send(message.encode('utf-8'))
        received_data = client_socket.recv(1024).decode('utf-8')
        print('Received from server:', received_data)

    client_socket.close()

start_client()

