# -*- coding: utf-8 -*-

"""
Author: XXM
date: 2020/8/18 19:19
desc: 
"""

import sys
import pyqtgraph as pg  # 画图的工具，安装方法：pip install pyqtgraph
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
import numpy as np


class PlotSin(QThread):
    signal = pyqtSignal(object)  # 定义信号，self.y 是 numpy.array，所以信号数据类型为 object

    def __init__(self, parent=None):
        super().__init__()
        self.y = None
        self.phase = 0

    def sin(self):
        self.x = np.arange(0, 3.0, 0.01)
        self.y = np.sin(2 * np.pi * self.x + self.phase)
        self.phase += 0.1
        QThread.msleep(200)  # 等待200毫秒

    def run(self):
        for _ in range(300):
            self.sin()
            self.signal.emit(self.y)  # 向连接槽发射信号 self.y


class PlotSin_MainWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.clock_time = 0
        self.timer = QTimer(self)  # 生成定时器
        self.timer.timeout.connect(self.clock)  # 绑定计时函数 self.clock

    def initUI(self):

        self.creatContorls("时间显示：")
        self.creatResult("函数绘制：")

        layout = QHBoxLayout()
        layout.addWidget(self.controlsGroup)
        layout.addWidget(self.resultGroup)
        self.setLayout(layout)
        self.beginButton.clicked.connect(self.clock_begin)
        self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle('Plot Sine')
        self.show()

    def creatContorls(self, title):
        self.controlsGroup = QGroupBox(title)
        self.beginButton = QPushButton("开始")

        numberLabel = QLabel("运行时间：")
        self.clockLabel = QLabel("")
        controlsLayout = QGridLayout()
        controlsLayout.addWidget(numberLabel, 0, 0)
        controlsLayout.addWidget(self.clockLabel, 0, 1)
        controlsLayout.addWidget(self.beginButton, 3, 0)
        self.controlsGroup.setLayout(controlsLayout)

    def creatResult(self, title):
        self.resultGroup = QGroupBox(title)
        self.guiplot = pg.PlotWidget()
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.guiplot, 0, 2, 2, 3)
        self.resultGroup.setLayout(gridLayout)

    def clock_begin(self):
        if not self.timer.isActive():
            self.recorder_thread = PlotSin()
            self.recorder_thread.signal.connect(self.displaySin)  # 绑定信号槽函数
            self.recorder_thread.start()  # 线程执行
            self.clock()
            self.timer.start(1000)
        else:
            self.beginButton.setText("开始")
            self.clockLabel.setText("")
            self.recorder_thread.terminate()  # 终止线程
            self.timer.stop()  # 终止定时器
            self.clock_time = 0
            text = str(self.clock_time) + "s"
            self.clockLabel.setText(text)

    def clock(self):
        text = str(self.clock_time) + "s"
        self.clockLabel.setText(text)
        if self.clock_time == 0:
            self.beginButton.setText("结束")

        self.clock_time += 1

    def plotSin(self, y):
        self.guiplot.clear()
        self.guiplot.plot(y)

    def displaySin(self, y):
        self.plotSin(y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PlotSin_MainWindow()
    window.show()
    sys.exit(app.exec_())