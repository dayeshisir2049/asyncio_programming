import asyncio

from common.helper import delay


async def main():
    results = await asyncio.gather(delay(3), delay(1))
    print(results)


asyncio.run(main())
