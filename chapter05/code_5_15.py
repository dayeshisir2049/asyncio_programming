import asyncio
import asyncpg

from chapter05 import get_db_connection


async def main():
    conn = await get_db_connection()
    query = "select product_id, product_name from product"

    async with conn.transaction():
        # NOTE: 游标需要在事务管理器上下文中启用
        async for product in conn.cursor(query):
            print(product)
            # 同普通的for,这里也可以执行break
            # break

    await conn.close()

    await conn.close()

asyncio.run(main())