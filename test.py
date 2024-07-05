#encoding=utf-8
from time import time


class TimeCounter(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            t = time()
            func()
            return print(f"time: {time() - t}")
        return wrapper

@TimeCounter('a', 'b')
def function():
    print("hello world")


function()
