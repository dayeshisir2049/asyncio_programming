import asyncio
import time

from utils.delay_functions import delay


async def main():
    start = time.time()
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))

    await sleep_for_three
    await sleep_again
    await sleep_once_more

    end = time.time()

    print(f'cost: {end - start: .2f}')

if __name__ == '__main__':
    asyncio.run(main())
