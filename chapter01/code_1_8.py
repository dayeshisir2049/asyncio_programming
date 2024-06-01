import threading
import time

import requests


def read_example():
    resp = requests.get('https://www.example.com')
    print(resp.status_code)


if __name__ == '__main__':
    thread_1 = threading.Thread(target=read_example)
    thread_2 = threading.Thread(target=read_example)

    start = time.time()
    thread_1.start()
    thread_2.start()

    print('all threads running')

    thread_1.join()
    thread_2.join()

    end = time.time()

    print(f'costs  {end - start:.2f}')
