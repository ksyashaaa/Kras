
import os, shutil, subprocess, socket

PORT = 9090
 
sock = socket.socket()
sock.bind(('', PORT))
sock.listen()
 
while True:
    print("Слушаем порт", PORT)
    conn, addr = sock.accept()
    print(addr)
    
    request = conn.recv(1024).decode()
    print(request)
    
    response = process(request)
    conn.send(response.encode())
    sock.close()

# HOST = 'localhost'
# PORT = 9090
 
# while True:
#     sock = socket.socket()
#     sock.connect((HOST, PORT))
    
#     request = input('myftp@shell$ ')
#     sock.send(request.encode())
    
#     response = sock.recv(1024).decode()
#     print(response)
    
#     sock.close()

# def process(req):
#     if req == 'pwd':
#         return os.getcwd()
#     elif req == 'ls':
#         return '; '.join(os.listdir())
#     else:
#         return 'bad request'