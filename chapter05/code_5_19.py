import asyncio

from chapter05 import get_db_connection


async def take(generator, to_take: int):
    item_count = 0
    async for item in generator:
        if item_count < to_take:
            item_count += 1
            yield item
        else:
            return


async def main():
    conn = await get_db_connection()
    async with conn.transaction():
        query = "select product_id, product_name from product"
        # 这里不能使用await conn.cursor(query)
        generator = conn.cursor(query)
        print(type(generator))

        async for item in take(generator, 10):
            print(item)

        print('Got the first ten products')

    await conn.close()


asyncio.run(main())
