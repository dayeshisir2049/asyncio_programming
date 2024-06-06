import time
from multiprocessing import Pool


def say_hello(name: str, delay: int = 0) -> str:
    start = time.time()
    time.sleep(delay)
    ret = f'Hi there, {name}'
    end = time.time()
    print(f'Finished with {name} in {end - start:.2f} seconds')
    return ret


if __name__ == '__main__':
    with Pool() as process_pool:
        start = time.time()
        hi_jeff = process_pool.apply_async(say_hello, ('Jeff', 3))
        hi_john = process_pool.apply_async(say_hello, ('John', 2))

        # 使用apply_async后，需要使用返回结果的get方法，如下图所示
        print(hi_jeff.get())
        print(hi_john.get())
        end = time.time()

        # 由于两个进程是并行执行的，总耗时是最长进程的耗时，例如3s
        print(f'Finished with {end - start:.2f} seconds')
