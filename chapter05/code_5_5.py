import asyncio
from random import sample
from typing import List, Tuple, Union

from chapter05 import get_db_connection


def load_common_words() -> List[str]:
    with open('./common_words.txt', 'r', encoding='utf-8') as f:
        return f.read().splitlines()


def generate_brand_names(words: List[str]) -> List[Tuple[Union[str,]]]:
    return [(words[index],) for index in sample(range(100), 100)]


async def insert_brands(common_words, conn) -> int:
    # executemany 协程接受一个SQL语句，和一个包含想要插入的值的元组列表
    # 可以使用$1,$2...$N语法来参数化SQL语句
    brands = generate_brand_names(common_words)
    insert_brands = "INSERT INTO brand VALUES (DEFAULT, $1)"
    return await conn.executemany(insert_brands, brands)


async def main():
    common_words = load_common_words()
    conn = await get_db_connection()
    await insert_brands(common_words, conn)


asyncio.run(main())
