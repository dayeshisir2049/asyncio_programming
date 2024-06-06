import asyncio

from common.helper import async_timed, delay


async def positive_integers_async(until: int):
    """
    异步生成器
    和同步相比，也就多了个async
    :param until:
    :return:
    """
    for i in range(1, until):
        await delay(i)
        yield i


@async_timed()
async def main():
    async_generator = positive_integers_async(10)
    print(type(async_generator))   # <class 'async_generator'>
    # 使用异步生产器的for循环
    async for number in async_generator:
        print(f'Got number: {number}')


asyncio.run(main())
