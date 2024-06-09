import asyncio
from asyncio import StreamReader
from typing import AsyncGenerator


async def read_until_empty(stream_reader: StreamReader) -> AsyncGenerator[str, None]:
    # stream_reader的readline协程一直等待，直到获取到一行数据
    while response := await stream_reader.readline():
        yield response.decode()


async def main():
    host: str = 'www.example.com'
    request: str = f"GET / HTTP/1.1\r\nConnection: close\r\nHost: {host}\r\n\r\n"

    # open_connection接受连接的主机地址和端口，以元组的形式返回stream_reader和stream_writer
    stream_reader, stream_writer = await asyncio.open_connection(host, 80)

    try:
        # stream_writer.write是一个普通的方法，底层是将写入数据放入写入缓存区中，有可能写入速度比发送速度快
        # 需要结合drain方法使用，drain确保写入的数据都发送出去了
        stream_writer.write(request.encode())
        await stream_writer.drain()

        response = [response async for response in read_until_empty(stream_reader)]

        print(''.join(response))
    except Exception as e:
        print(e)
    finally:
        stream_writer.close()
        await stream_writer.wait_closed()


asyncio.run(main())
