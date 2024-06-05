import asyncio

from aiohttp import ClientSession

from chapter04 import fetch_status
from common.helper import async_timed


@async_timed()
async def main():
    async with ClientSession() as session:
        url = 'https://example.com'
        fetchers = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
        ]
        # 入参是 协程列表
        # return_when 默认是 ALL_COMPLETED,所有协程完成才返回
        # 返回值包含已经完成（成功/异常）列表、未外出列表
        done, pending = await asyncio.wait(fetchers)

        # 由于默认是全部协程都完成，才返回，所以下述打印中，done是2，pending是0
        print(f'Done task count: {len(done)}')
        print(f'Pending task count: {len(pending)}')

        for done_task in done:
            result = await done_task
            print(f'Done task: {result}')


asyncio.run(main())
