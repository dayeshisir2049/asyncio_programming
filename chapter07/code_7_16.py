import hashlib
import os
import random
import string
import time


def random_password(length: int) -> bytes:
    ascii_letters = string.ascii_lowercase.encode('utf-8')
    return b''.join(bytes(random.choice(ascii_letters)) for _ in range(length))


passwords = [random_password(10) for _ in range(10000)]


def hash(password: bytes) -> str:
    salt = os.urandom(16)
    return str(hashlib.scrypt(password, salt=salt, n=2048, p=1, r=8))


start = time.time()
for password in passwords:
    hashed = hash(password)
    # print(f'{password} {hashed}')
end = time.time()

print(f'finished in {end - start:.4f} seconds')
