import asyncio

import aiohttp

from chapter04 import fetch_status


async def main():
    async with aiohttp.ClientSession() as session:
        api_a = asyncio.create_task(fetch_status(session, 'https://example.com'))
        api_b = asyncio.create_task(fetch_status(session, 'https://example.com', delay=15))

        done, pending = await asyncio.wait([api_a, api_b], timeout=1)
        for task in done:
            if task is api_b:
                print('API B too slow, cancelling')
                task.cancel()


asyncio.run(main())
