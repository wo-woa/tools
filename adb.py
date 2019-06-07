# -*- coding: utf-8 -*-
import os
import time

adb_path = 'D:/AndroidSdk/platform-tools/'


def click_ok():
    os.system(adb_path + "adb shell input keyevent 23")
    time.sleep(0.5)


def swipe_down(x1=200, y1=1200, x2=200, y2=600):
    os.system(adb_path + "adb shell input swipe " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2))
    time.sleep(0.5)


def click_power():
    os.system(adb_path + "adb shell input keyevent 26")
    time.sleep(0.5)


def click(x, y):
    os.system(adb_path + "adb shell input tap " + str(x) + " " + str(y))
    time.sleep(0.5)


def click_home():
    os.system(adb_path + "adb shell input keyevent 3")
    time.sleep(0.5)


def click_back():
    os.system(adb_path + "adb shell input keyevent 4")
    time.sleep(0.5)


# click(902, 1667)
# click(930,1546)
# time.sleep(11)
# click(918,1714)#4
# click(874,1590)#领取
while True:
    # click(527, 1702)  # 召唤
    # click(527, 1702)  # 召唤
    # click(510, 1608)  # 逛店铺
    click(902, 1667)
    click(920, 1368)
    time.sleep(11)
    click(977, 1114)  # 领取
    click(547, 1576)  # 收下
    click_back()
