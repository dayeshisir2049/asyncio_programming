import asyncio
import socket


class ConnectedSocket:
    def __init__(self, server_socket: socket.socket):
        self.server_socket = server_socket
        self.conn = None

    async def __aenter__(self):
        print(f'Entering context manager, waiting for connection...')
        loop = asyncio.get_running_loop()
        conn, address = await loop.sock_accept(self.server_socket)
        self.conn = conn
        print(f'Accepted connection from {address}')
        return conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f'Exiting context manager')
        self.conn.close()
        print('Closed connection')


async def main():
    loop = asyncio.get_event_loop()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(('127.0.0.1', 8000))
    server_socket.setblocking(False)
    server_socket.listen()

    async with ConnectedSocket(server_socket) as conn:
        data = await loop.sock_recv(conn, 1024)
        print(data)
        await loop.sock_sendall(conn, data)


asyncio.run(main())
