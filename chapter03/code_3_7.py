import selectors
import socket
from selectors import SelectorKey
from typing import List, Tuple

selector = selectors.DefaultSelector()

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(('127.0.0.1', 8000))
server_socket.setblocking(False)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)

while True:
    # 创建一个将在1s后超时的选择器
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)

    # 如果没有事件，则将其输出，发生超时时，会出现这种情况
    if len(events) == 0:
        print(f'No events, waiting a bit more!')
        continue

    for event, _ in events:
        # 获取事件的套接字，该套接字存储在fileobj字段中
        event_socket = event.fileobj

        # 如果事件套接字与服务器套接字相同，我们就知道这是一次连接尝试
        if event_socket == server_socket:
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f'I got a connection from {address}')
            # 注册与选择器连接的客户端
            # 一次性的，触发后需要再次注册
            selector.register(connection, selectors.EVENT_READ)
        else:
            # 如果事件套接字不是服务器套接字，则从客户端接受数据，并将其回显
            data = event_socket.recv(1024)
            print(f'I got some data: {data}')
            event_socket.send(data)

