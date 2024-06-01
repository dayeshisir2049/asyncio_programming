import asyncio

from chapter02.utils.delay_functions import delay


async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))

    result = await sleep_for_three
    print(type(result))


if __name__ == '__main__':
    asyncio.run(main())
