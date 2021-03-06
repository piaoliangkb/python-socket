from socket import AF_INET, SOCK_STREAM, socket
from concurrent.futures import ThreadPoolExecutor

# A server side client to response user's message.
def echo_client(sock, client_addr):
    """
    Handle a client connection
    """
    print(f"Got connection form {client_addr}")
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print("Client closed connection")
    sock.close()
    

def echo_server(addr):
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)

if __name__ == "__main__":
    echo_server(("", 15000))
