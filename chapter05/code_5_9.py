import asyncio

from chapter05 import get_db_connection


async def main():
    conn = await get_db_connection()

    # 启动数据库事务管理器
    async with conn.transaction():
        await conn.execute("INSERT INTO brand VALUES (DEFAULT, 'brand_1')")
        await conn.execute("INSERT INTO brand VALUES (DEFAULT, 'brand_2')")

    query = "select brand_name from brand where brand_name like 'brand%'"
    brands = await conn.fetch(query)
    print(brands)

    await conn.close()


asyncio.run(main())