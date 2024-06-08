import asyncio

import requests

from common.helper import async_timed


def get_status_code(url: str) -> int:
    r = requests.get(url)
    return r.status_code


@async_timed()
async def main():
    tasks = [asyncio.to_thread(get_status_code, 'https://www.example.com') for _ in range(10)]
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
