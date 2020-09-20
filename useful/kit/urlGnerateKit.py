# -*- coding: utf-8 -*-

"""
Author: XXM
date: 2020/8/20 18:59
desc: 
"""
import re
import requests
from lxml import etree


def get_url_and_pass(text):
    pattern = 'https://pan.baidu.com/s/([\w-]+)\s'
    data = re.search(pattern, text)
    if data:
        url = data.group(1).strip()
    else:
        url = '匹配失败'
    # pass_pattern = r'验证码.+?(\w+)|提取码.+?(\w+)|密码.+?(\w+)|\[sell=\d+?,\d+?\](.+?)\['
    # data = re.search(pass_pattern, text)
    data = re_pass(text)
    if data:
        password = data.strip()
    else:
        password = '匹配失败'
    return url, password


def re_pass(txt):
    pattern_list = '\[sell=\d+?,\d+?\](.+?)\[|验证码.+?(\w+)|提取码.+?(\w+)|密码.+?(\w+)'
    for pattern in pattern_list.split('|'):
        data = re.search(pattern, txt)
        if data:
            return data.group(1)
    return ''


def get_real_url(share, pwd):
    url = "http://pan.naifei.cc/?share={share}&pwd={pwd}".format(share=share, pwd=pwd)
    html = requests.get(url)
    ehtml = etree.HTML(html.text)
    real_url = ehtml.xpath('/html/body/table/tbody/tr/td[3]/a/@href')
    return real_url[0]


if __name__ == '__main__':
    pass
