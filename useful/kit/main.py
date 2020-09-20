# -*- coding: utf-8 -*-

"""
Author: XXM
date: 2020/8/17 14:09
desc: 
"""
from PySide2.QtCore import QObject, Signal
from PySide2.QtGui import QIcon, QColor
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
import json
import sys
import re
import requests
from lxml import etree
import webbrowser
import time
import multiprocessing as mp
import traceback
import simulateAppKit
from coverKit import cover
from NewThreadKit import NewThread
import fileRenamKite
import urlGnerateKit


class SettinInterface:

    def __init__(self):
        self.ui = QUiLoader().load('main.ui')
        self.main_content = []
        self.thread = object
        self.ui.pushButton.clicked.connect(self.get_url_and_pass)
        self.ui.pushButton_2.clicked.connect(self.get_real_url)
        self.ui.pushButton_3.clicked.connect(self.open_browse)
        self.ui.pushButton_4.clicked.connect(self.simulate_app)
        self.ui.pushButton_5.clicked.connect(self.get_content)
        self.ui.pushButton_6.clicked.connect(self.copy_to_baidu)
        self.ui.pushButton_7.clicked.connect(self.get_cover)
        self.ui.pushButton_8.clicked.connect(self.rename)
        # self.ui.pushButton_9.clicked.connect(self.stop)

    def get_url_and_pass(self):
        text = self.ui.plainTextEdit.toPlainText()
        url, pwd = urlGnerateKit.get_url_and_pass(text)
        self.ui.textEdit.setText(url)
        self.ui.textEdit_2.setText(pwd)

    def get_real_url(self):
        share = self.ui.textEdit.toPlainText()
        pwd = self.ui.textEdit_2.toPlainText()
        real_url = urlGnerateKit.get_real_url(share, pwd)
        self.ui.textEdit_3.setText(real_url)

    def open_browse(self):
        webbrowser.open(self.ui.textEdit_3.toPlainText())

    def simulate_app(self):
        text = self.ui.plainTextEdit_2.toPlainText()
        main_password, self.main_content = simulateAppKit.simulate_app(text)
        self.ui.plainTextEdit_3.setPlainText(main_password)

    def get_content(self):
        for i in self.main_content:
            self.ui.plainTextEdit_3.appendPlainText(str(i))

    def copy_to_baidu(self):
        self.ui.plainTextEdit.setPlainText(self.ui.plainTextEdit_3.toPlainText())
        self.ui.tabWidget.setCurrentIndex(0)

    def get_cover(self):
        path = self.ui.plainTextEdit_4.toPlainText()
        c = cover(path)
        c.getImgFolderPaths(path)
        c.mutiprocess_run(self.ui.plainTextEdit_5)

    def rename(self):
        path = self.ui.plainTextEdit_7.toPlainText()
        main_file_list = fileRenamKite.get_name_list(path)
        fileRenamKite.rename_by_sort(main_file_list, path, indent=3)
        # self.thread = NewThread()
        # self.thread.signal.connect(self.display)
        # self.thread.start()

    def display(self, y):
        self.ui.plainTextEdit_6.appendPlainText(str(y))

    def stop(self):
        # self.thread.terminate()
        c = QColor(255, 0, 0)
        # 设定 RGB 颜色
        # 设置输出颜色
        self.ui.plainTextEdit_6.setStyleSheet(u'background-color:rgb(255,255,0); color:rgb(255,0,0)')
        self.ui.plainTextEdit_6.appendPlainText("1111")


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('./config/图标.ico'))
    music_dowload = SettinInterface()
    music_dowload.ui.show()
    app.exec_()
