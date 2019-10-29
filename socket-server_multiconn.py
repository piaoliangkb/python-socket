# coding=UTF-8
'''
@Description: socketserver for receiving data until client close it
@Author: piaoliangkb
@Date: 2019-04-18 14:54:34
@LastEditTime: 2019-04-18 16:15:01
@reference: https://stackoverflow.com/questions/8627986/how-to-keep-a-socket-open-until-client-closes-it
'''
import socketserver
import time


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):

        while True:
            self.data = self.request.recv(1024)
            if not self.data:
                break
            localtime = time.asctime(time.localtime(time.time()))
            print("receive data [{}] from {} at {}".format(
                self.data, self.client_address, localtime))

            # return upper data from requeste
            # self.request.sendall(self.data.upper())


class ThreadTCPserver(socketserver.ThreadingMixIn, socketserver.TCPServer):

    def __init__(self, ipport, tcphandleclass):
        socketserver.TCPServer.__init__(self, ipport, tcphandleclass)
        print("listrning on ", ipport)


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9996
    server = ThreadTCPserver((HOST, PORT), TCPHandler)
    server.serve_forever()