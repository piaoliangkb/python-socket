from socket import *
import time

# 创建socket
tcpClientSocket = socket(AF_INET, SOCK_STREAM)

# # 客户端心跳维护
# # 长链接在没有数据通信时，定时发送心跳，维持链接状态
# # 如果TCP在10秒内没有进行数据传输，则发送嗅探包，
# # 每隔3秒发送一次，共发送5次。如果5次都没收到相应，则表示连接已中断。
# tcpClientSocket.setsockopt(SOL_SOCKET, SO_KEEPALIVE, 1)
# tcpClientSocket.setsockopt(IPPROTO_TCP, TCP_KEEPIDLE, 10)
# tcpClientSocket.setsockopt(IPPROTO_TCP, TCP_KEEPINTVL, 3)
# tcpClientSocket.setsockopt(IPPROTO_TCP, TCP_KEEPCNT, 5)

# 链接服务器
serAddr = ('127.0.0.1', 9996)
tcpClientSocket.connect(serAddr)


while True:

    localtime = time.asctime(time.localtime(time.time()))
    data = input()
    data = (data + " at {}".format(localtime)).encode("utf-8")
    tcpClientSocket.send(data)

    # recvdata = tcpClientSocket.recv(1024)
    # print("data received : {} at time {}".format(recvdata, time.time()))


# 关闭套接字
tcpClientSocket.close()