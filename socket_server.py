from socket import *
import socketserver

# 创建socket
tcpSerSocket = socket(AF_INET, SOCK_STREAM)

# 绑定本地信息
address = ('', 28888)
tcpSerSocket.bind(address)

# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
tcpSerSocket.listen(5)

# https://docs.python.org/3/library/socket.html#socket-objects
#
# socket.accept() returns a tuple (conn, address)
# where conn is a new socket object useable to send 
# and receive data on the connection, address is the 
# address bound to the socket on the other hand of the 
# connection.
newSocket, clientAddr = tcpSerSocket.accept()

while True:

    # 接收对方发送过来的数据，最大接收1024个字节
    recvData = newSocket.recv(1024)

    # 如果接收的数据的长度为0，则意味着客户端关闭了链接
    if len(recvData) <= 0:
        break
    else:
        print('recv:', recvData)

        # # 发送一些数据到客户端
        # sendData = input("send:")
        # newSocket.send(bytes(sendData.encode("utf8")))
        # # 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
        # newSocket.close()
        # break

# 关闭监听套接字，只要这个套接字关闭了，就意味着整个程序不能再接收任何新的客户端的连接
tcpSerSocket.close()
