import asyncio
import asyncpg
from asyncpg.transaction import Transaction

from chapter05 import get_db_connection


async def main():
    conn = await get_db_connection()
    transaction: Transaction = conn.transaction()

    # 开启事务
    await transaction.start()

    try:
        # await conn.execute("INSERT INTO brand VALUES (DEFAULT, 'brand_12_1')")
        # await conn.execute("INSERT INTO brand VALUES (DEFAULT, 'brand_12_2')")
        await conn.execute("INSERT INTO brand VALUES (9999, 'brand_12_1')")
        await conn.execute("INSERT INTO brand VALUES (9999, 'brand_12_2')")
    except asyncpg.PostgresError:
        print('Errors, rolling back transaction')
        await transaction.rollback()
    else:
        print('No errors, committing transaction')
        await transaction.commit()

    query = "select * from brand where brand_name like 'brand_12_%'"
    brands = await conn.fetch(query)
    print(brands)

    await conn.close()

asyncio.run(main())