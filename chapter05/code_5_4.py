import asyncio
from typing import List

from asyncpg import Record

from chapter05 import get_db_connection


async def main():
    conn = await get_db_connection()
    # await conn.execute("INSERT INTO brand VALUES (DEFAULT, 'Levis')")
    # await conn.execute("INSERT INTO brand VALUES (DEFAULT, 'Seven')")

    # async.Record 的行为类似字典，fetch获取的结果是多个
    brand_query = 'SELECT brand_id, brand_name FROM brand'
    result: List[Record] = await conn.fetch(brand_query)
    for brand in result:
        print(f'id: {brand["brand_id"]}, name: {brand["brand_name"]}')

    # fetchrow获取的结果是一个，但是，返回的类型，asyncpg.Record
    one_row = await conn.fetchrow('SELECT brand_id, brand_name FROM brand')
    print(type(one_row))
    print(f'id: {one_row["brand_id"]}, name: {one_row["brand_name"]}')

    await conn.close()


asyncio.run(main())
