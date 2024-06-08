import asyncio
import functools
import hashlib
import os
import random
import string
from concurrent.futures import ThreadPoolExecutor
from common.helper import async_timed

def random_password(length: int) -> bytes:
    ascii_letters = string.ascii_lowercase.encode('utf-8')
    return b''.join(bytes(random.choice(ascii_letters)) for _ in range(length))


def hash(password: bytes) -> str:
    salt = os.urandom(16)
    return str(hashlib.scrypt(password, salt=salt, n=2048, p=1, r=8))

@async_timed()
async def main():
    loop = asyncio.get_event_loop()
    passwords = [random_password(10) for _ in range(10000)]
    with ThreadPoolExecutor(max_workers=10) as executor:
        tasks = [loop.run_in_executor(executor, functools.partial(hash, password)) for password in passwords]
        await asyncio.gather(*tasks)


asyncio.run(main())
