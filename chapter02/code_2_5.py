import asyncio


async def hello_world_message() -> str:
    await asyncio.sleep(1)
    return 'Hello World!'


async def main() -> None:
    messsage = await hello_world_message()
    print(messsage)


if __name__ == '__main__':
    asyncio.run(main())
