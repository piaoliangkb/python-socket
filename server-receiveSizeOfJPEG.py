# coding = utf-8
import socket
import time
import os

HOST = ''
PORT = 8868
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)
print("Listening at port number:", PORT)
index = 1

while True:
	conn, addr = s.accept()
	# print("Connection from ", addr)
	# accpet函数默认阻塞线程，直到有客户端请求连接
	# conn是新的套接字对象，可以用来接收和发送数据
	# addr是连接客户端的地址
	while True:
		# socket传输格式规定：图片字节字符串长度 + 图片字节数字符串 + 图片信息
		# 例如： 6 + 123456 + ....... (lenthOfpicbitlength + filelength + data)
		# 表示： 图片大小位123456字节，共6位，随后为图片的字节流内容
		try:
			lengthOfpicbitlength = conn.recv(1)
		except OSError:
			break
		print(lengthOfpicbitlength)
		lengthOfpicbitlength = lengthOfpicbitlength.decode()
		if lengthOfpicbitlength == "":
			break
		data = conn.recv(int(lengthOfpicbitlength))
		data = data.decode()
		print(data)
		if data == "":
			# socket关闭后会传递空串
			break
		filelength = int(data)
		print("This file size is :" + str(filelength))
		recvlength = 0
		while recvlength != filelength:
			if filelength - recvlength > 1024:
				data = conn.recv(1024)
				recvlength += 1024
			else:
				data = conn.recv(filelength - recvlength)
				recvlength = filelength
			# 将字节流写入文件（时间消耗比较大，每秒接收帧的数量降低）
			# 不写入文件每秒接收帧数提升较大
			try:
				filename = "picture" + str(index) + ".jpg"
				with open(filename, "ab") as file1:
					file1.write(data)
			except PermissionError:
				index -= 1
				break
		index += 1
		conn.close()
s.close()  