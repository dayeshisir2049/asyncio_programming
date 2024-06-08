import functools
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from common.helper import async_timed

def get_status_code(url: str) -> int:
    r = requests.get(url)
    return r.status_code

@async_timed()
async def main():
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        urls = ['https://www.example.com' for _ in range(100)]
        # 如果每个函数的入参不一样，可以使用partial函数，绑定参数
        # 但是，如果每个函数的参数是一样的，也可也直接使用如下方式传递进去入参
        # tasks = [loop.run_in_executor(pool, functools.partial(get_status_code, url)) for url in urls]
        tasks = [loop.run_in_executor(pool, get_status_code, 'https://www.example.com') for _ in range(100)]

        results = await asyncio.gather(*tasks)
        print(results)


asyncio.run(main())