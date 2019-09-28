# -*- coding: utf-8 -*-
import os
import time

adb_path = 'D:/AndroidSdk/platform-tools/'


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
    print('click' + memo)
    time.sleep(0.5)


def click_all(x, y, memo=''):
    os.system(adb_path + "adb shell input tap " + str(x) + " " + str(y))


def click_home():
    os.system(adb_path + "adb shell input keyevent 3")
    print('click_home')
    time.sleep(0.5)


def click_back():
    os.system(adb_path + "adb shell input keyevent 4")
    print('click_back')
    time.sleep(0.5)



def zhang_yu():
    for i in range(40):
        click(928, 1797, '点击任务')
        click(911, 1526, '随机逛店铺')
        time.sleep(11)
        click_back()
        print(str(i) + '次')


def dian_pu_yuan():
    local = [
        [538, 217],
        [235, 472],
        [863, 471],
        [535, 716],
        [228, 973],
        [848, 992],
        [539, 1230],
        [240, 1491],
        [851, 1489],
        [534, 1751]
    ]
    for i in range(2):
        for j in local:
            click(j[0], j[1])
            time.sleep(11)
            click_back()
            print('点击' + str(j))
        swipe_down(544, 1155, 544, 0)


def dian_pu_zheng():
    local = [
        [541, 226],
        [185, 400],
        [879, 400],
        [541, 631],
        [185, 825],
        [874, 821],
        [542, 1065],
        [184, 1271],
        [882, 1281],
        [534, 1450]
    ]
    for i in range(5):
        for j in local:
            click(j[0], j[1] + 730)
            time.sleep(11)
            click_back()
            print('点击' + str(j))
        swipe_down(544, 1022, 544, 0)


def brawl_star_drop():
    click(2028, 973)  # 开始
    n = 1
    while True:
        print('正在进行第' + str(n) + '次')
        n = n + 1
        time.sleep(16)
        click(1201, 1004, '退出')  # 退出
        time.sleep(1)
        click(1832, 974, '继续')  # 继续
        time.sleep(3)
        click(1427, 987, '再来')  # 再来


# dian_pu_yuan()
# dian_pu_zheng()
brawl_star_drop()
