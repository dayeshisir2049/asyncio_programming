import asyncio

from aiohttp import ClientSession

from chapter04 import fetch_status
from common.helper import async_timed


@async_timed()
async def main():
    """
    as_completed可以设置超时（以秒为单位）
    但是as_completed超时返回后，协程仍然在运行，没有同步取消
    :return:
    """
    async with ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://www.example.com', 1),
            fetch_status(session, 'https://www.example.com', 10),
            fetch_status(session, 'https://www.example.com', 10),
        ]

        for done_task in asyncio.as_completed(fetchers, timeout=4):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print('We got a timeout error')

        for task in asyncio.tasks.all_tasks():
            print(task)


asyncio.run(main())
