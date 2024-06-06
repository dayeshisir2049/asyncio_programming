import asyncio
import asyncpg

from chapter05 import get_db_connection


async def main():
    conn = await get_db_connection()
    async with conn.transaction():
        query = "select product_id, product_name from product"
        cursor = await conn.cursor(query=query)
        # NOTE：游标不能双向游动，只能forward
        await cursor.forward(500)
        products = await cursor.fetch(100)
        for product in products:
            print(product)

    await conn.close()


asyncio.run(main())