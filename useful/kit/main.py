# -*- coding: utf-8 -*-

"""
Author: XXM
date: 2020/8/17 14:09
desc: 
"""
from PySide2.QtGui import QIcon, QColor
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *
import json

import fileRenamKite
import imageCompresKit
import simulateAppKit
from coverKit import Cover


class SettinInterface:

    def __init__(self):
        self.ui = QUiLoader().load('main.ui')
        self.main_content = []
        self.data = {}
        self.thread = object
        self.load_config()
        self.ui.widget1_getpassword.clicked.connect(self.simulate_app)
        self.ui.widget1_getdetail.clicked.connect(self.get_content)
        # self.ui.pushButton_6.clicked.connect(self.copy_to_baidu)
        # self.ui.pushButton_7.clicked.connect(self.get_cover)
        self.ui.widget3_rename.clicked.connect(self.rename)
        self.ui.widget4_compress.clicked.connect(self.compress)
        self.ui.pushButton.clicked.connect(self.test)

    def simulate_app(self):
        text = self.ui.widget1_url.text()
        main_password, self.main_content = simulateAppKit.simulate_app(text)
        self.ui.widget1_content.setPlainText(main_password)

    def get_content(self):
        for i in self.main_content:
            self.ui.widget1_content.appendPlainText(str(i))

    def copy_to_baidu(self):
        self.ui.plainTextEdit.setPlainText(self.ui.plainTextEdit_3.toPlainText())
        self.ui.tabWidget.setCurrentIndex(0)

    def get_cover(self):
        path = self.ui.plainTextEdit_4.toPlainText()
        c = Cover(path)
        c.getImgFolderPaths(path)
        c.mutiprocess_run(self.ui.plainTextEdit_5)

    def rename(self):
        path = self.ui.widget3_url.text()
        self.thread = fileRenamKite.RenameThread(path)
        self.thread.signal.connect(self.widget3_display)
        self.thread.start()
        # main_file_list = fileRenamKite.get_name_list(path)
        # fileRenamKite.rename_by_sort(main_file_list, path, indent=3)
        # self.thread = NewThread()
        # self.thread.signal.connect(self.display)
        # self.thread.start()

    def widget3_display(self, y):
        self.ui.widget3_content.appendPlainText(str(y))

    def compress(self):
        path = self.ui.widget4_url.text()
        type = int(self.ui.widget4_combobox_type.currentIndex())
        mb = int(self.ui.widget4_lineedit_target.text())
        step = int(self.ui.widget4_lineedit_init_rate.text())
        quality = int(self.ui.widget4_lineedit_compress_rate.text())
        self.thread = imageCompresKit.CompressThread(path, type, mb, step, quality)
        self.thread.signal.connect(self.widget4_display)
        self.thread.start()

    def widget4_display(self, y):
        self.ui.widget4_content.appendPlainText(str(y))

    def stop(self):
        # self.thread.terminate()
        c = QColor(255, 0, 0)
        # 设定 RGB 颜色
        # 设置输出颜色
        self.ui.plainTextEdit_6.setStyleSheet(u'background-color:rgb(255,255,0); color:rgb(255,0,0)')
        self.ui.plainTextEdit_6.appendPlainText("1111")

    def load_config(self):
        # try:
        with open('.\\config\\settin.json', 'r') as file:
            self.data = json.load(file)
        self.ui.widget4_combobox_type.setCurrentIndex(int(self.data["widget4"]["type"]))
        self.ui.widget4_lineedit_target.setText(self.data["widget4"]["target"])
        self.ui.widget4_lineedit_init_rate.setText(self.data["widget4"]["init_rate"])
        self.ui.widget4_lineedit_compress_rate.setText(self.data["widget4"]["compress_rate"])
        # except Exception as e:
        #     print(e)
        #     print("load fail")

    def closeEvent(self):
        # try:
        widget4 = {}
        widget4["type"] = self.ui.widget4_combobox_type.currentIndex()
        widget4["target"] = self.ui.widget4_lineedit_target.text()
        widget4["init_rate"] = self.ui.widget4_lineedit_init_rate.text()
        widget4["compress_rate"] = self.ui.widget4_lineedit_compress_rate.text()
        self.data["widget4"] = widget4
        with open('.\\config\\settin.json', 'w') as file:
            json.dump(self.data, file)
        # except:
        #     print("save fail")

    def test(self):
        print(self.ui.widget4_url.text())
        print(self.ui.widget4_lineedit_target.text())


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('./config/图标.ico'))
    music_dowload = SettinInterface()
    music_dowload.ui.show()
    app.aboutToQuit.connect(music_dowload.closeEvent)
    app.exec_()
