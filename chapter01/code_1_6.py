import threading
import time

def fib(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibs_with_threads():
    fortieth_thead = threading.Thread(target=fib, args=(40, ))
    forty_first_thread = threading.Thread(target=fib, args=(41, ))

    fortieth_thead.start()
    forty_first_thread.start()

    fortieth_thead.join()
    forty_first_thread.join()


if __name__ == '__main__':
    start = time.time()
    fibs_with_threads()
    print(f'{time.time() - start: .4f}')