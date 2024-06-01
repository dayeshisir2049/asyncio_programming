import asyncio


async def add_one(number: int) -> int:
    return number + 1


async def main():
    one_plus_one = await add_one(1)
    two_plus_two = await add_one(2)

    print(one_plus_one)
    print(two_plus_two)


if __name__ == '__main__':
    asyncio.run(main())
