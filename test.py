#encoding=utf-8
from time import time


class TimeCounter(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        t = time()
        self.func()
        return print(f"time: {time() - t}")

