import asyncio
import functools
import time
from typing import Callable, Any


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args: Any, **kwargs: Any) -> Any:
            print(f'starting {func} with {args} with {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total_time = end - start
                print(f'finished {func} in {total_time:.4f} seconds')

        return wrapped

    return wrapper


async def delay(delay_seconds: int) -> int:
    print(f'sleeping for {delay_seconds} second(s)')
    await asyncio.sleep(delay_seconds)
    print(f'finished sleeping for {delay_seconds} second(s)')

    return delay_seconds
