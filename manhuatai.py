# -*- coding: utf-8 -*-

import requests
from lxml import etree
import re
import os
import time
import shutil


def download_img(url, name):
    try:
        data = requests.get(url)
        if data.status_code == 404:
            raise Exception('invalid url')
        else:
            with open(name + '.jpg', 'wb') as file:
                file.write(data.content)
    except IOError:
        print('net error')
    except Exception as err:
        print(err)
        print(url)


def get_list(url):
    data = requests.get(url)
    html = etree.HTML(data.text.encode('iso-8859-1').decode('utf-8'))
    # text_list = html.xpath('//*[@id="topic1"]/li/a/@title')
    text_list = html.xpath('//*[@id="topic1"]/li/a/span/text()')
    chapter_list = []
    pattern = '(.+?)\((\d+)P'
    for each in text_list:
        if each.find('为梦想付费') != -1:
            continue
        each_map = {}
        result = re.search(pattern, each)
        if result:
            each_map['name'] = result.group(1)
            each_map['count'] = result.group(2)
        else:
            raise Exception('not match')
        chapter_list.append(each_map)
    print('一共有' + str(len(chapter_list)) + '章')
    chapter_list.reverse()
    return chapter_list


def download_list(chapter_list):
    i = 1
    for each in chapter_list:
        print('正在下载' + each['name'] + ',一共' + each['count'] + '张')
        if not os.path.exists(each['name']):
            os.makedirs(each['name'])
        os.chdir(each['name'])
        for count in range(int(each['count'])):
            count = count + 1
            if not os.path.exists(str(count) + '.jpg'):
                # 不知道如果有超过100的怎么办
                print('开始下载第' + str(count) + '张')
                url = img_url.format(chapter=str(i).zfill(2), page=str(count))
                download_img(url, str(count))
            else:
                print('第' + str(count) + '张已经存在')
        i = i + 1
        os.chdir('..')


def run(name, chapter_list):
    if not os.path.exists(name):
        os.makedirs(name)
    os.chdir(name)
    download_list(chapter_list)
    print('下载完成')


img_url = 'https://mhpic.jumanhua.com/comic/L%2F%E9%BE%99%E6%97%8F%E2%85%A0%2F{chapter}%E8%AF%9D%2F{page}.jpg-mht.middle.webp'

url = 'https://www.manhuatai.com/longzu/'
name = '龙族'
chapter_list = get_list(url)
run(name, chapter_list)
# download_img('https://mhpic.jumanhua.com/comic/L%2F%E9%BE%99%E6%97%8F%E2%85%A1%2F01%E8%AF%9D%2F0.jpg-mht.middle.webp','1')
