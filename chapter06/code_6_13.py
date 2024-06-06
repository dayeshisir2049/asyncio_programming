import asyncio
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Value

shared_counter: Value


def init(counter: Value):
    global shared_counter
    shared_counter = counter


def increment():
    with shared_counter.get_lock():
        shared_counter.value += 1


async def main():
    counter = Value('i', 0)
    # 进程池中的初始化函数，和初始化参数，保证在进程池中创建的进程都执行一遍
    # 也就保证了每个进程的内存中，都有一个全局的shared_counter指向counter
    # 在进程的主方法，increment中，所有进程操作的都是同一个对象
    with ProcessPoolExecutor(initializer=init, initargs=(counter,)) as pool:
        tasks = [asyncio.get_running_loop().run_in_executor(pool, increment) for _ in range(10)]
        await asyncio.gather(*tasks)
        print(counter.value)


if __name__ == '__main__':
    asyncio.run(main())
