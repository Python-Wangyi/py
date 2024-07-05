#encoding=utf-8
from time import time


def time_counter(f):
    def wrapper():
        t1 = time()
        f()
        t2 = time() - t1
        return print(f"运行时间：{t2}")
    return wrapper


# @time_counter
def mainloop(n: str):
    print(n)

mainloop()
