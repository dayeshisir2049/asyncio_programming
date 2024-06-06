import time
from concurrent.futures import ProcessPoolExecutor


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1
    end = time.time()
    print(f'Finished counting {count_to} in {round(end - start, 2)} seconds')
    return counter


if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        # executor.map是按照入参的顺序，等待完成的，当耗时较长的任务（10000000）在中间时
        # 即使后面的任务（22），已经完成，也需要等待长耗时任务完成，才会返回
        # numbers = [1, 3, 5, 22, 10000000]
        numbers = [1, 3, 5, 10000000, 22]
        for result in executor.map(count, numbers):
            print(result)
