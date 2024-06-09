import asyncio

from common.helper import delay


async def main():
    while True:
        delay_time = input('Enter a time to sleep:')
        # 循环内部没有主动让出GIL机制，导致协程任务得不到调度
        # 手动调用await asyncio.sleep(0)可以让出GIL，调度协程
        asyncio.create_task(delay(int(delay_time)))
        # await asyncio.sleep(0)


asyncio.run(main())
