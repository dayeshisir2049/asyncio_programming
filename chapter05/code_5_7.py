import asyncio

import asyncpg

from common.helper import async_timed

product_query = \
    """
    select p.product_id,
       p.product_name,
       p.brand_id,
       s.sku_id,
       pc.product_color_name,
       ps.product_size_name
from product as p
join sku as s on s.product_id=p.product_id
join product_color as pc on pc.product_color_id = s.product_color_id
join product_size as ps on ps.product_size_id = s.product_size_id
where p.product_id=100
    """


@async_timed()
async def query_product(pool, delay: int = 0):
    await asyncio.sleep(delay)
    # 确保是在acquire返回的conn中查询，保证查询结束，上下文管理器能及时回收连接池
    async with pool.acquire() as conn:
        return await conn.fetchrow(product_query)


async def main():
    async with asyncpg.create_pool(
            host='localhost',
            port=5432,
            user='postgres',
            password='pg123456',
            database='postgres',
            min_size=3,
            max_size=5,
    ) as pool:
        tasks = [query_product(pool, second//3) for second in range(1, 18)]
        await asyncio.gather(*tasks)


asyncio.run(main())
