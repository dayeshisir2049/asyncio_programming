import asyncio
import asyncpg
from common.helper import async_timed
from typing import List, Dict
from concurrent.futures import ProcessPoolExecutor

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

async def query_product(pool):
    async with pool.acquire() as conn:
        # 异步执行pg查询操作
        return await conn.fetchrow(product_query)

@async_timed()
async def query_products_concurrent(pool, queries_num):
    queries = [query_product(pool) for _ in range(queries_num)]
    # 这里的await是等到所有的查询执行完成，一起返回
    return await asyncio.gather(*queries)


def run_in_new_loop(num_queries: int) -> List[Dict]:
    async def run_queries():
        async with asyncpg.create_pool(
            host='localhost',
            port=5432,
            user='postgres',
            password='pg123456',
            database='postgres',
            min_size=6,
            max_size=10,
        ) as pool:
            return await query_products_concurrent(pool, num_queries)

    print(f'run_in_new_loop({num_queries})')
    results = [dict(result) for result in asyncio.run(run_queries())]
    return results

@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    pool = ProcessPoolExecutor()
    # run_in_executor 在之前的例子中，不能传递参数，其实是可以传递参数的，args接受的参数，会透传到执行函数run_in_new_loop里面
    tasks = [loop.run_in_executor(pool, run_in_new_loop, 1000) for _ in range(5)]
    print(type(tasks))
    print(type(tasks[0]))

    # 以下执行会报错
    # all_tasks = await asyncio.gather(*tasks)
    # total_queries = sum([len(result) for result in all_tasks])

    total_queries = 0
    for task in tasks:
        res = await task
        total_queries += len(res)

    print(f'Retrieved {total_queries} products from the product database')


if __name__ == '__main__':
    asyncio.run(main())
