import asyncpg


async def get_db_connection():
    conn = await asyncpg.connect(
        host='localhost',
        port=5432,
        user='postgres',
        password='pg123456',
        database='postgres',
    )
    return conn