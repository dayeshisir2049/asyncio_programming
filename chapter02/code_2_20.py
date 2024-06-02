import asyncio

import requests

from common.helper import async_timed


@async_timed()
async def get_example_status() -> int:
    return requests.get('http://www.example.com').status_code


@async_timed()
async def main():
    task_one = asyncio.create_task(get_example_status())
    task_two = asyncio.create_task(get_example_status())

    task_three = asyncio.create_task(get_example_status())

    await task_one
    await task_two
    await task_three


asyncio.run(main())
