import socket


HOST = ''
PORT = 8866
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)
print("Listening at port number:", PORT)
conn, addr = s.accept()
# accpet函数默认阻塞线程，直到有客户端请求连接
# conn是新的套接字对象，可以用来接收和发送数据
# addr是连接客户端的地址
print("Connection from ", addr)
while True:  
    data = conn.recv(1024)
    print('Received:', data.decode())
    conn.sendall("i have got the data".encode())  
conn.close()
s.close()  