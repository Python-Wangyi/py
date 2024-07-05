#encoding=utf-8
import tkinter as tk


def create_borderless_window():
    # 创建窗口实例
    window = tk.Tk()

    # 使窗口无边框
    window.overrideredirect(True)

    # 设置窗口的大小和位置
    window.geometry("200x100+100+100")

    # 添加一些内容到窗口
    label = tk.Label(window, text="无边框窗口", highlightcolor='red')
    label.pack()

    # 启动事件循环
    window.mainloop()


create_borderless_window()
