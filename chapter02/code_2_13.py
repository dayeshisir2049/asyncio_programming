import asyncio

from utils.delay_functions import delay


async def main():
    task = asyncio.create_task(delay(10))

    try:
        # asyncio.shield 函数包装任务，防止传入的协程被取消
        result = await asyncio.wait_for(asyncio.shield(task), 5)

        # 如果直接wait_for协程，时间介绍时，会取消协程
        # result =await asyncio.wait_for(task, 5)
        print(result)
    except asyncio.TimeoutError:
        print("task took longer than five seconds, it will finished soon")
        # 虽然asyncio.shield 在超时时，没有取消协程，这里需要再次await
        result = await task
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
