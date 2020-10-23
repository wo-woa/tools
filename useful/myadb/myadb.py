# -*- coding: utf-8 -*-

"""
Author: XXM
date: 2020/10/23 20:27
desc: 
"""

import os
import time


def click_ok():
    os.system(adb_path + "adb shell input keyevent 23")
    print('click_ok')
    time.sleep(0.5)


def swipe_down(x1=200, y1=1200, x2=200, y2=600):
    os.system(adb_path + "adb shell input swipe " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2))
    print('swipe_down')
    time.sleep(0.5)


def click_power():
    os.system(adb_path + "adb shell input keyevent 26")
    print('click_power')
    time.sleep(0.5)


def click(x, y, memo=''):
    os.system(adb_path + "adb shell input tap " + str(x) + " " + str(y))
    print('click ' + memo)
    time.sleep(0.5)


def click_back():
    os.system(adb_path + "adb shell input keyevent 4")
    print('click_back')
    time.sleep(0.5)


def click_home():
    os.system(adb_path + "adb shell input keyevent 3")
    print('click_home')
    time.sleep(0.5)


if __name__ == '__main__':
    adb_path = os.getcwd() + '/'
    # adb_path = 'D:/AndroidSdk/platform-tools/'
    name = input("请输入脚本名字（默认script）:")
    name = 'script' if name == '' else name
    with open(name, encoding='utf-8') as file:
        txt = file.read()
        exec(txt)
    input("按任意键退出")