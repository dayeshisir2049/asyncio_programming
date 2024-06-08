import asyncio
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

import requests

from common.helper import async_timed

# 在线程中，需要手动申明锁，在操作共享内存对象时，申请锁
counter_lock = Lock()
counter = 0


def get_status_code(url: str) -> int:
    global counter
    resp = requests.get(url)
    with counter_lock:
        counter += 1

    return resp.status_code


async def reporter(request_count: int):
    global counter
    while counter < request_count:
        print(f'Finished {counter}/{request_count} requests')
        await asyncio.sleep(.5)


@async_timed()
async def main():
    request_count = 100
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        tasks = [loop.run_in_executor(pool, get_status_code, 'https://www.example.com') for _ in range(request_count)]
        reporter_task = asyncio.create_task(reporter(request_count))

        results = await asyncio.gather(*tasks)
        await reporter_task

        print(results)


asyncio.run(main())
