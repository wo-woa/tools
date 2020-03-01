# -*- coding: utf-8 -*-
import os
import time

adb_path = 'D:/AndroidSdk/platform-tools/'
# adb_path = os.getcwd()+'/'


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

def click_all(x, y, memo=''):
    os.system(adb_path + "adb shell input tap " + str(x) + " " + str(y))


def click_home():
    os.system(adb_path + "adb shell input keyevent 3")
    print('click_home')
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


def miao_bi():
    click(916, 1700, '领喵币')
    for i in range(20):
        click(878, 1088, '一')
        swipe_down(500,1000,500,200)
        time.sleep(15)
        click_back()
        print(str(i) + '次')
    for i in range(4):
        click(878, 1278, '二')
        swipe_down(500, 1000, 500, 200)
        time.sleep(15)
        click_back()
    for i in range(2):
        click(878, 1462, '三')
        swipe_down(500,1000,500,200)
        time.sleep(15)
        click_back()
    for i in range(2):
        click(878, 1647, '四')
        swipe_down(500,1000,500,200)
        time.sleep(15)
        click_back()
    # click(878, 1834, '五')


def miao_bi2():
    click(916, 1700, '领喵币')
    for i in range(23):
        click(878, 1278, '二')
        time.sleep(1)
        swipe_down(500,1000,500,200)
        time.sleep(16)
        click_back()
        print(str(i) + '次')
    for i in range(4):
        click(878, 1462, '三')
        time.sleep(1)
        swipe_down(500, 1000, 500, 200)
        time.sleep(15)
        click_back()
    for i in range(3):
        click(878, 1647, '四')
        time.sleep(1)
        swipe_down(500,1000,500,200)
        time.sleep(15)
        click_back()
    for i in range(3):
        click(878, 1834, '五')
        time.sleep(1)
        swipe_down(500,1000,500,200)
        time.sleep(15)
        click_back()
    # click(878, 1834, '五')
    # click(878, 1088, '一')
def jd_mid(num,x,y,txt):
    for i in range(num):
        click(x,y,txt)
        time.sleep(1)
        click_back()
        time.sleep(1)
        click(551,1578,'朕知道了')
def jd():
    click(956, 1747,'领金币')
    time.sleep(1)
    jd_mid(23, 923, 953,'一')
    jd_mid(3, 923, 1177, '二')
    jd_mid(25, 923, 1400, '三')
    jd_mid(4, 923, 1610, '四')
    jd_mid(4, 923, 2053, '六')


brawl_star_drop()
# miao_bi()
# miao_bi2()
# jd()
input("已结束")