import asyncio
import time
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import List


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1
    end = time.time()
    print(f'Finished counting to {count_to} in {round(end - start, 2)} seconds')
    return counter


async def main():
    with ProcessPoolExecutor() as process_pool:
        loop: AbstractEventLoop = asyncio.get_event_loop()
        nums = [1, 3, 5, 22, 10000000, 33]
        calls: List[partial[int]] = [partial(count, num) for num in nums]
        call_coros = []

        for call in calls:
            # run_in_executor接受进程池（也可以是线程池）和一个可调用对象（可调用对象不支持传参，需要使用偏函数冻结入参）
            # 并在池子中调用可调用对象，返回一个awaitable对象
            # 返回值可以用在await语句或者接受await语句的api中
            call_coros.append(loop.run_in_executor(process_pool, call))

        results = await asyncio.gather(*call_coros)
        for result in results:
            print(result)

        # results = asyncio.as_completed(call_coros)
        # for result in results:
        #     print(await result)


if __name__ == '__main__':
    asyncio.run(main())
