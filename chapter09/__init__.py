import asyncpg
from aiohttp.web_app import Application
from asyncpg import Pool

DB_KEY='database'
async def create_database_pool(app: Application):
    print('Creating database pool...')
    pool: Pool = await asyncpg.create_pool(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        password='pg123456',
        database='postgres',
        min_size=6,
        max_size=10,
    )
    # 将app作为字典使用，使用DB_KEY存储初始化的数据库连接池
    app[DB_KEY] = pool


async def destory_database_pool(app: Application):
    print('Destorying database pool...')
    pool: Pool = app[DB_KEY]
    await pool.close()