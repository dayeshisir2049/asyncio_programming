from queue import Queue
from tkinter import Tk, Label, Entry, ttk
from typing import Optional

from chapter07.code_7_13 import StressTest


class LoadTester(Tk):

    def __init__(self, loop, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # tk 和 asyncio 线程同步，借助队列实现解耦，免除竞争条件
        self._queue = Queue()
        self._refresh_ms = 25

        self._loop = loop
        self._load_test: Optional[StressTest] = None
        self.title('URL Requester')

        self._url_label = Label(self, text='URL')
        self._url_label.grid(column=0, row=0)

        self._url_field = Entry(self, width=10)
        self._url_field.grid(column=1, row=0)

        self._request_label = Label(self, text='Number of requests')
        self._request_label.grid(column=0, row=1)

        self._request_field = Entry(self, width=10)
        self._request_field.grid(column=1, row=1)

        # 当被单击时，提交按钮将调用_start方法
        self._submit = ttk.Button(self, text='Submit', command=self._start)
        self._submit.grid(column=2, row=1)

        self._pb_label = Label(self, text='Progress:')
        self._pb_label.grid(column=0, row=3)

        self._pb = ttk.Progressbar(self, orient='horizontal', length=200, mode='determinate')
        self._pb.grid(column=1, row=3, columnspan=2)

    def _update_bar(self, pct: int):
        """"
        更新进度条，从0到100的百分比
        这个方法只在主线程中使用
        :param pct:
        """
        print(f'update bar: {pct}%')
        if pct == 100:
            self._pb['value'] = pct
            self._load_test = None
            self._submit['text'] = 'Submit'
        else:
            self._pb['value'] = pct
            self.after(self._refresh_ms, self._poll_queue)

    def _queue_update(self, completed_requests: int, total_requests: int):
        """
        给压力测试准备的回调函数，将更新进度到队列中
        :param completed_requests:
        :param total_requests:
        :return:
        """
        self._queue.put(int(completed_requests / total_requests * 100))

    def _poll_queue(self):
        # 尝试从队列中获取更新进度，如果队列有更新，则更新进度条
        if not self._queue.empty():
            percent_complete = self._queue.get()
            self._update_bar(percent_complete)
        else:
            if self._load_test:
                self.after(self._refresh_ms, self._poll_queue)

    def _start(self):
        if self._load_test is None:
            print('New stress test')
            self._submit['text'] = 'Cancel'
            test = StressTest(
                self._loop,
                self._url_field.get(),
                int(self._request_field.get()),
                self._queue_update
            )
            # 每25毫秒轮询一次队列更新
            self.after(self._refresh_ms, self._poll_queue)
            test.start()
            self._load_test = None
        else:
            print('cancel stress test')
            self._load_test.cancel()
            self._load_test = None
            self._submit['text'] = 'Submit'
