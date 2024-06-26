from threading import Thread, RLock
from typing import List

list_lock = RLock()

def sum_list(int_list: List[int]) -> int:
    print('Waiting to acquire lock...')
    with list_lock:
        print('Acquired lock')
        if len(int_list) == 0:
            return 0

        else:
            head, *tail = int_list
            print('Summing rest of list')

            return head + sum_list(tail)


thread = Thread(target=sum_list, args=([i for i in range(100)],))
thread.start()
thread.join()
