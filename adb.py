# -*- coding: utf-8 -*-
import os
import time

adb_path = 'D:/AndroidSdk/platform-tool/'


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

i=1
print('start...')
while (True):
    click(800, 350)
    click_back()
    click_back()
    print('click '+str(i)+' times')
    i=i+1
    time.sleep(44)
    click(800, 350)
    time.sleep(43)


