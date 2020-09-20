# -*- coding: utf-8 -*-

"""
Author: XXM
date: 2020/8/13 18:39
desc: 
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import re
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.center()
        self.show()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('baidu')

        font = QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)

        self.content = QLabel('content：', self)
        self.content.setGeometry(QRect(10, 0, 80, 100))
        self.content.setFont(font)
        self.contentEdit = QTextEdit(self)
        self.contentEdit.setGeometry(QRect(80, 0, 390, 100))

        self.button = QPushButton("click", self)
        self.button.setGeometry(200, 100, 100, 50)
        self.button.clicked.connect(self.button_click)

        # result = QLabel('result', self)
        # result.move(10, 250)
        # resultEdit = QLineEdit(self)
        # resultEdit.move(60, 250)

        # qbtn = QPushButton('Quit', self)
        # qbtn.setToolTip('This is a <b>QPushButton</b> widget')
        # qbtn.clicked.connect(QCoreApplication.instance().quit)
        # qbtn.resize(qbtn.sizeHint())
        # qbtn.move(50, 50)

    # 控制窗口显示在屏幕中心的方法
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 关闭窗口弹出框
    def closeEvents(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def button_click(self):
        input_text = self.contentEdit.toPlainText()
        pattern_share = 'pan.baidu.com/s/(\w+)'
        pattern_pwd = '提取码: (\w+)'
        data = re.search(pattern_share, input_text)
        if data:
            share = data.group(1)
        else:
            pass
        data = re.search(pattern_pwd, input_text)
        if data:
            pwd = data.group(1)
        else:
            pass
        url = 'http://pan.naifei.cc/?share={share}&pwd={pwd}'

        print(url.format(share=share, pwd=pwd))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
