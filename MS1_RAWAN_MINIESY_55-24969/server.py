import socket
import threading

PORT = 5605
ADDR = ('127.0.0.1', PORT)
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def threaded(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    while True:
        data = conn.recv(1024).decode(FORMAT)
        
        if not data:
            break
        
        
        response = "Message received by the server"
        response= data.upper()
        conn.send(response.encode(FORMAT))
    
   
    conn.close()
    print(f"[CONNECTION CLOSED] {addr} disconnected.")

def start_server():
    
    server.listen()
    print("Server is starting...")
    
    while True:
        conn, addr = server.accept()
        threading.Lock().acquire()
        thread = threading.Thread(target=threaded, args=(conn, addr))
        thread.start()
        
        
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

start_server()