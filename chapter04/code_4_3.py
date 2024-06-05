import asyncio

import aiohttp
from aiohttp import ClientSession

from common.helper import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    # 设置一秒钟的超时，此处的超时设置会覆盖session级别的超时设置
    timeout = aiohttp.ClientTimeout(total=1)
    async with session.get(url, timeout=timeout) as resp:
        return resp.status


async def main():
    # 除了设置总超时时间，连接超时时间，还有如下时间设置：
    # sock_read: Optional[float] = None
    # sock_connect: Optional[float] = None
    session_timeout = aiohttp.ClientTimeout(total=.1, connect=.1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        status = await fetch_status(session, url='https://example.com')
        print(f'status: {status}')


asyncio.run(main())
