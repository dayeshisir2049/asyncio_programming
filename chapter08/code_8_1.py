import asyncio
from asyncio import Future, AbstractEventLoop, Transport
from typing import Optional


class HTTPGetClientProtocol(asyncio.Protocol):
    def __init__(self, host: str, loop: AbstractEventLoop):
        self._host = host
        self._future: Future = loop.create_future()
        self._transport: Optional[Transport] = None
        self._response_buffer: bytes = b''

    async def get_response(self):
        # 等待内部的future，直到得到服务器的响应
        return await self._future

    def _get_request(self) -> bytes:
        # 创建HTTP请求
        request = f"GET / HTTP/1.1\r\nConnection: close\r\nHost: {self._host}\r\n\r\n"
        return request.encode('utf-8')

    def connection_made(self, transport: Transport):
        print(f'Connection made to {self._host}')
        self._transport = transport
        # 一旦建立了连接，使用传输来发送请求
        self._transport.write(self._get_request())

    def data_received(self, data: bytes):
        print('Data received')
        # 一旦得到数据，将其保存到内部缓存区
        self._response_buffer += data

    def eof_received(self) -> Optional[bool]:
        self._future.set_result(self._response_buffer.decode('utf-8'))
        return False

    def connection_lost(self, exc: Optional[Exception]):
        # 如果连接正常关闭，，则什么也不做，否则，通过异常完成future
        if exc is not None:
            self._future.set_exception(exc)
            return

        print('Connection closed with error.')
