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
        hi_jeff = process_pool.apply(say_hello, ('Jeff', 3))
        hi_john = process_pool.apply(say_hello, ('John', 2))

        print(hi_jeff)
        print(hi_john)
        end = time.time()

        # process_pool.apply是串行执行的，因此总耗时是2+3=5s
        print(f'Finished with {end - start:.2f} seconds')
