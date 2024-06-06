import asyncio
import logging

from chapter05 import get_db_connection


async def main():
    conn = await get_db_connection()

    # 启动数据库事务管理器
    try:
        async with conn.transaction():
            insert_brand = "INSERT INTO brand VALUES (9999, 'big_brand')"
            await conn.execute(insert_brand)
            await conn.execute(insert_brand)
    except Exception as e:
        logging.exception('Error while running transaction')
    finally:
        query = "select brand_name from brand where brand_name like 'big_%'"
        brands = await conn.fetch(query)
        print(f'Query result was: {brands}')

    await conn.close()


asyncio.run(main())
