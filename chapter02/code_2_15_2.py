import asyncio


class MyAwaitable:
    """
    自定义一个awaitable对象：
    - 定义__await__方法，在方法中返回可迭代对象
    """
    def __next__(self):
        raise StopIteration('end')

    def __iter__(self):
        return self

    def __await__(self):
        print("Hello Awaitable")
        return self


async def main():
    await MyAwaitable()


if __name__ == "__main__":
    asyncio.run(main())
