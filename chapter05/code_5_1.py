import asyncio

from chapter05 import get_db_connection


async def main():
    conn = await get_db_connection()

    version = conn.get_server_version()
    print(f'Connected! Postgres version: {version}')
    await conn.close()

asyncio.run(main())