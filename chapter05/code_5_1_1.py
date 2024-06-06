import asyncio

import aiomysql


async def connect_main():
    conn = await aiomysql.connect(host='localhost', port=3306, user='root', password='123456', db='asyncio')
    cursor = await conn.cursor()
    await cursor.execute('SELECT 12')
    result = await cursor.fetchone()
    print(result)
    await cursor.close()
    conn.close()


async def pool_main():
    pool = await aiomysql.create_pool(host='localhost', port=3306, user='root', password='123456', db='asyncio')
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute('SELECT 12')
            result = await cursor.fetchone()
            print(result)


asyncio.run(pool_main())
