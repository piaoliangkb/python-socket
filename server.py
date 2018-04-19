import socket
import time


HOST = ''
PORT = 8868
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)
print("Listening at port number:", PORT)

while True:
    conn, addr = s.accept()
    print("Connection from ", addr)
    # accpet函数默认阻塞线程，直到有客户端请求连接
    # conn是新的套接字对象，可以用来接收和发送数据
    # addr是连接客户端的地址
    index = 1
    while True:
        index = 1
        data = conn.recv(1024)
        with open("picture" + str(index)+ ".jpg","ab") as file1:
            file1.write(data)
            index +=1
        print('Received picture {}'.format(str(index)))
    # conn.sendall("i have got the data".encode())  
    conn.close()
s.close()  