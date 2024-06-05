import asyncio

import aiohttp

from chapter04 import fetch_status
from common.helper import async_timed


@async_timed()
async def main():
    """
    gather异常处理
    - return_exceptions = false, gather默认方式，协程抛出异常，在等待gather时也会抛出异常
    - return_exceptions = true, gather将返回任何异常，作为等待返回结果的一部分
    :return:
    """
    async with aiohttp.ClientSession() as session:
        urls = ['http://example.com', 'python://example.com']
        # 生产一个请求的协程列表
        requests = [fetch_status(session, url) for url in urls]
        # 等待所有操作完成
        result = await asyncio.gather(*requests, return_exceptions=True)

        exception_result = [res for res in result if isinstance(res, Exception)]
        success_result = [res for res in result if not isinstance(res, Exception)]

        print(result)
        print(exception_result)
        print(success_result)


asyncio.run(main())
