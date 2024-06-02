import asyncio

from common.helper import async_timed


@async_timed()
async def cpu_bound_work() -> int:
    count = 0
    for i in range(100000000):
        count += 1

    return count


@async_timed()
async def main():
    """
    使用asyncio运行两个CPU密集型的任务，效果相当于穿行运行，执行完第一个，才执行第二个
    :return:
    """
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())

    await task_one
    await task_two


asyncio.run(main())
