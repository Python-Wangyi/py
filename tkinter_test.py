#encoding=utf-8
from tkinter import *


class MainLove(Tk):
    def __init__(self):
    screenWidth = root.winfo_screenwidth()  # 获取显示区域的宽度
    screenHeight = root.winfo_screenheight()  # 获取显示区域的高度
    width = 300  # 设定窗口宽度
    height = 160  # 设定窗口高度
    left = (screenWidth - width) / 2
    top = (screenHeight - height) / 2

    # 宽度x高度+x偏移+y偏移
    # 在设定宽度和高度的基础上指定窗口相对于屏幕左上角的偏移位置
    root.geometry("%dx%d+%d+%d" % (width, height, left, top))
