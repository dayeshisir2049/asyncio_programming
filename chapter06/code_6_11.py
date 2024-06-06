from multiprocessing import Process, Value


def increment_value(shared_int: Value):
    shared_int.value += 1


if __name__ == '__main__':
    integer = Value('i', 0)

    # 启动100个进程，也没有出错
    proc_num = 100
    procs = [Process(target=increment_value, args=(integer,)) for _ in range(proc_num)]
    [p.start() for p in procs]
    [p.join() for p in procs]

    print(integer.value)
    assert integer.value == proc_num
