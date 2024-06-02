import asyncio
from asyncio import Future


def normal():
    """
    - 生成Future对象
    - 完成业务逻辑后，设置结果
    - set_result调用之后，done方法返回True,result方法放回设置的结果
    :return:
    """
    my_future = Future()

    print(f'Is my_future done? {my_future.done()}')

    my_future.set_result(1)

    print(f'Is my_future done? {my_future.done()}')
    print(f'What is the result of my_future? {my_future.result()}')


def call_result_without_set_result():
    """
    result方法调用，必须在set_result方法之后，否则，返回InvalidStateError异常
    :return:
    """
    my_future = Future()

    print(f'Is my_future done? {my_future.done()}')

    print(f'Is my_future done? {my_future.done()}')

    try:
        print(f'What is the result of my_future? {my_future.result()}')
    except asyncio.exceptions.InvalidStateError as e:
        print(str(e))


def set_exception():
    """
    future也可以设置异常
    在业务逻辑出现异常时，设置异常，调用方在try_catch中处理异常
    ** 注意：当调用set_result后，就不可以设置异常 **
    :return:
    """
    my_future = Future()

    print(f'Is my_future done? {my_future.done()}')

    # 通过set_result设置future的值
    # my_future.set_result(1)
    my_future.set_exception(Exception("something went wrong"))

    try:
        print(f'What is the result of my_future? {my_future.result()}')
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    normal()
    set_exception()
    call_result_without_set_result()
