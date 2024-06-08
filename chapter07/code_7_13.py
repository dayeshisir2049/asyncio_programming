import asyncio
from concurrent.futures import Future
from asyncio import AbstractEventLoop
from typing import Callable, Optional
from aiohttp import ClientSession

class StressTest:
    def __init__(self,
                 loop: AbstractEventLoop,
                 url: str,
                 total_requests: int,
                 callback: Callable[[int, int], None]):
        self._completed_requests: int = 0
        self._load_test_future: Optional[Future] = None
        self._loop = loop
        self._url = url
        self._total_requests = total_requests
        self._callback = callback
        self._refresh_rate = total_requests // 100

    def start(self):
        # 开始发送请求，并存储future，以便以后可以在需要时取消
        # run_coroutine_threadsafe接收一个协程，以线程安全的方式执行，返回一个future，用来访问返回的结果
        self._load_test_future = asyncio.run_coroutine_threadsafe(self._make_requests(), self._loop)

    def cancel(self):
        if self._load_test_future:
            # 接收一个python函数，并在下一轮事件循环中，以线程安全的方式调度
            self._loop.call_soon_threadsafe(self._load_test_future.cancel)

    async def _get_url(self, session: ClientSession, url: str):
        try:
            await session.get(url)
        except Exception as e:
            print(e)

        self._completed_requests += 1
        if self._completed_requests % self._refresh_rate == 0 or self._completed_requests == self._total_requests:
            # 一旦完成1%，使用已经完成的请求数，和总的请求数，回调回调函数ss
            self._callback(self._completed_requests, self._total_requests)

    async def _make_requests(self):
        async with ClientSession() as session:
            reqs = [self._get_url(session, self._url) for _ in range(self._total_requests)]
            await asyncio.gather(*reqs)
