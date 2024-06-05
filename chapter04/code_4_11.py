import asyncio
import logging

import aiohttp

from chapter04 import fetch_status
from common.helper import async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        good_request = fetch_status(session, 'https://www.example.com')
        bad_request = fetch_status(session, 'python://bad')

        fetchers = [
            asyncio.create_task(good_request),
            asyncio.create_task(bad_request),
        ]
        done, pending = await asyncio.wait(fetchers)
        print(f'Done tasks: {len(done)}')
        print(f'Pending tasks: {len(pending)}')

        for done_task in done:
            # 继续这么调用，会抛出异常
            # result = await done_task
            # print(f'Done task: {result}')

            # 可以直接使用 exception和result来获取异常、正常返回值
            if done_task.exception():
                logging.error("Request got an exception", exc_info=done_task.exception())
            else:
                print(done_task.result())


asyncio.run(main())