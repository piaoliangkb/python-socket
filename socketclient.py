import socket
import sys

HOST = '127.0.0.1'
# 服务器主机的IP地址
PORT = 8866
# 服务器主机端口号

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# "AF_INET"是IPV4网络协议的套接字类型
# "SOCK_STREAM"提供面向连接的稳定数据传输
try:
	s.connect((HOST, PORT))
except Exception as e:
	print("Server not found or not open")
	sys.exit()

while True:
	c = input("input the content you want to send:")
	s.sendall(c.encode())
	# 发送数据
	data = s.recv(1024)
	# 从服务端接收1024个字节的返回信息
	data = data.decode()
	print('Received form server:', data)
s.close()