import socket
import sys
import os



HOST = '127.0.0.1'
# HOST = '127.0.0.1'
# 服务器主机的IP地址
PORT = 8868
# 服务器主机端口号

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# "AF_INET"是IPV4网络协议的套接字类型
# "SOCK_STREAM"提供面向连接的稳定数据传输
try:
	s.connect((HOST, PORT))
except Exception as e:
	print("Server not found or not open")
	sys.exit()

with open("IMG_7514.jpg","rb") as file:
	content = file.read()
s.sendall(content)


while True:
	c = input("input the content you want to send:")
	s.sendall("456687".encode())
	# 发送数据
	data = s.recv(1024)
	# 从服务端接收1024个字节的返回信息
	data = data.decode()
	print('Received form server:', data)
s.close()