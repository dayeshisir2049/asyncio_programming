import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(('127.0.0.1', 8000))
server_socket.listen()
server_socket.setblocking(False)  # 将服务器套接字设置为非阻塞

connections = []
try:
    while True:
        try:
            conn, addr = server_socket.accept()
            conn.setblocking(False)  # 将客户端套接字设置为非阻塞
            print(f'I got a connection from {addr}')
            connections.append(conn)
        except BlockingIOError:
            pass

        for conn in connections:
            buffer = b''
            while buffer[-2:] != b'\r\n':
                try:
                    # 此处不增加try-catch模块，会报错：BlockingIOError: [WinError 10035] 无法立即完成一个非阻止性套接字操作。
                    data = conn.recv(2)
                    if not data:
                        break
                    else:
                        print(f'I got data: {data}')
                        buffer += data
                except BlockingIOError:
                    pass
            print(f'All the data is {buffer}')
            conn.send(buffer)
finally:
    server_socket.close()
