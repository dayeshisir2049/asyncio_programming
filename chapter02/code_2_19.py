import asyncio

from common.helper import async_timed, delay


@async_timed()
async def cpu_bound_work() -> int:
    count = 0
    for i in range(100000000):
        count += 1
    return count


@async_timed()
async def main():
    """
    执行两个CPU密集型任务，然后是一个IO操作，由于CPU密集型工作不会主动释放GIL，
    执行的效果是，串行执行两个CPU密集型任务，然后执行IO操作，总耗时9s+（2.6 + 2.7 + 4）
    如果将IO操作最先提交，然后是两个CPU密集型操作，由于IO操作会主动释放GIL，执行效果是：
    IO操作 和 两个CPU密集型操作并发执行，总好事5s+ (2.6 + 2.7)
    :return:
    """
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    delay_task = asyncio.create_task(delay(4))

    await delay_task
    await task_one
    await task_two


asyncio.run(main())
