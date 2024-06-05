import asyncio

from aiohttp import ClientSession

from chapter04 import fetch_status
from common.helper import async_timed


@async_timed()
async def main():
    """
    不同于gather需要等待所有协程都完成才一次性返回,as_completed在协程完成时，立即返回
    :return:
    """
    async with ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://www.example.com', 1),
            fetch_status(session, 'https://www.example.com', 1),
            fetch_status(session, 'https://www.example.com', 10),
        ]

        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)


asyncio.run(main())
