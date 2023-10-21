import socket 
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
port = 5605
client.connect(('127.0.0.1',port))
while True :
    message=input("enter your message or enter CLOSE SOCKET:")
    client.send(bytes(message,'utf-8'))
    server_msg=client.recv(1024)
    if message=="CLOSE SOCKET":
        client.close()
        break
    print(server_msg.decode('utf-8'))