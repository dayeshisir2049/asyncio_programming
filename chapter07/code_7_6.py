import asyncio

import requests

from common.helper import async_timed


def get_status_code(url: str) -> int:
    r = requests.get(url)
    return r.status_code


@async_timed()
async def main():
    loop = asyncio.get_event_loop()
    # run_in_executor，executor是None时，使用默认执行器，默认执行器是ThreadPoolExecutor
    # 除非调用loop.set_default_executor设置默认执行器
    tasks = [loop.run_in_executor(None, get_status_code, 'https://www.example.com') for _ in range(100)]

    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
