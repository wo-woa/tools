# -*- coding: utf-8 -*-

"""
Author: XXM
date: 2020/8/18 20:51
desc: 
"""
# PySide2 引入线程类和信号
from PySide2.QtCore import QThread, Signal  # 注意区别就在于这里的信号是 Signal，和 PyQt5 不一样，而线程类是一样的
from multiprocessing import Pool
import time, threading


class NewThread(QThread):
    signal = Signal(object)  # 自定义信号，其中 object 为信号承载数据的类型

    def __init__(self, parent=None):
        super().__init__()
        self.x = 0  # 线程中自定义变量

    # 线程内可自定义其他函数
    def custom_function(self):
        # self.kit.appendPlainText(str(self.x))
        self.x += 1
        time.sleep(0.4)
        # QThread.msleep(1000)

    # new_thread = NewThread()

    # 通过 new_thread.start() 调用此 run() 函数
    def run(self):
        for _ in range(300):
            self.custom_function()
            self.signal.emit(self.x)  # 发射信号


if __name__ == '__main__':
    new_thread = NewThread()

    new_thread.start()  # 为线程分配资源，让它执行

    # 下面两个都是停止执行，但我一般用第二个
    new_thread.wait()
    new_thread.terminate()
