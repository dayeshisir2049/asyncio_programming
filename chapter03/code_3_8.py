import asyncio
import socket
from asyncio import AbstractEventLoop


async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    buffer = b''
    while data := await loop.sock_recv(connection, 1024):
        buffer += data
        if buffer.startswith(b'boom\r\n'):
            raise Exception("Unexpected network error")

        if buffer[-2:] == b'\r\n':
            print(f'{connection} {buffer}')
            await loop.sock_sendall(connection, buffer)
            buffer = b''


async def listen_for_connection(server_socket: socket, loop: AbstractEventLoop) -> None:
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'Got a connection from {address}')
        asyncio.create_task(echo(connection, loop))


async def main() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(('127.0.0.1', 8000))
    server_socket.setblocking(False)
    server_socket.listen()

    await listen_for_connection(server_socket, asyncio.get_event_loop())


asyncio.run(main())
