import asyncio

import aiohttp

from chapter04 import fetch_status
from common.helper import async_timed


@async_timed()
async def main():
    """
    gather可以确保结果返回结果的顺序
    :return:
    """
    async with aiohttp.ClientSession() as session:
        urls = ['http://example.com' for _ in range(100)]
        # 生产一个请求的协程列表
        requests = [fetch_status(session, url) for url in urls]
        # 等待所有操作完成
        status_code = await asyncio.gather(*requests)

        print(status_code)


asyncio.run(main())
