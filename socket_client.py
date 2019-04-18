from socket import *
import time


def set_keepalive_linux(sock, after_idle_sec=1, interval_sec=3, max_fails=5):

    """Set TCP keepalive on an open socket.

    It activates after 1 second (after_idle_sec) of idleness,
    then sends a keepalive ping once every 3 seconds (interval_sec),
    and closes the connection after 5 failed ping (max_fails), or 15 seconds

    TCP_KEEPIDLE : The time (in seconds) the connection needs to remain idle
    before TCP starts sending keepalive probes; 每空闲多少秒，就发送keepalive信息

    TCP_KEEPINTVL : The time (in seconds) between individual keepalive probes
    keepalive消息的时间间隔

    TCP_KEEPCNT :  The maximum number of keepalive probes TCP should send
    before dropping the connection; 发送多少个keepalive消息失败之后就关闭连接

    ----------------------------------------------------------------

    上述为Linux系统的参数，通过输入 sysctl -A |grep keepalive 指令，可以得到这些参数的默认值：

    TCP_KEEPINTVL -> net.ipv4.tcp_keepalive_intvl = 75      -- 间隔多少秒发一次嗅探包(75秒)
    TCP_KEEPCNT   -> net.ipv4.tcp_keepalive_probes = 9      -- 嗅探包一共发几次
    TCP_KEEPIDLE  -> net.ipv4.tcp_keepalive_time = 7200     -- TCP连接空闲多少秒后发嗅探包(2小时)

    如果TCP连接2小时（7200秒）内没有数据传输，则发送嗅探包，
    每隔75秒发送一次，共重试9次。9次对方都没响应，则表明此连接已死。

    """ 

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, after_idle_sec)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, interval_sec)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, max_fails)


# 创建socket
tcpClientSocket = socket(AF_INET, SOCK_STREAM)

# 客户端心跳维护
# 长链接在没有数据通信时，定时发送心跳，维持链接状态
# 如果TCP在10秒内没有进行数据传输，则发送嗅探包，
# 每隔3秒发送一次，共发送5次。如果5次都没收到相应，则表示连接已中断。
tcpClientSocket.setsockopt(SOL_SOCKET, SO_KEEPALIVE, 1)
tcpClientSocket.setsockopt(IPPROTO_TCP, TCP_KEEPIDLE, 10)
tcpClientSocket.setsockopt(IPPROTO_TCP, TCP_KEEPINTVL, 3)
tcpClientSocket.setsockopt(IPPROTO_TCP, TCP_KEEPCNT, 5)

# 链接服务器
serAddr = ('127.0.0.1', 28888)
tcpClientSocket.connect(serAddr)

while True:

    localtime = time.asctime(time.localtime(time.time()))
    data = "hello, sending data at {}".format(localtime).encode("utf-8")
    tcpClientSocket.send(data)
    print(data)
    # 间隔较久发送一次数据包
    time.sleep(600)


# 关闭套接字
tcpClientSocket.close()
