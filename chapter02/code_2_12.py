import asyncio

from utils.delay_functions import delay


async def main():
    delay_task = asyncio.create_task(delay(2))
    try:
        # asyncio.wait_for 接受协程或者任务对象，以及以秒为单位的指定的超时时间
        # 返回一个协程，超时时，引发TimeoutError异常
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Got a timeout')
        print(f'Was the task cancelled? {delay_task.cancelled()}')


if __name__ == '__main__':
    asyncio.run(main())
