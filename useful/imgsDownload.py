# -*- coding: utf-8 -*-

"""
Author: XXM
date: 2020/8/11 9:58
desc:
"""

import os
import requests
import re
from lxml import etree
# from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor, as_completed


def get_img_urls(url):
    """
    获取图片链接和名字
    :param url:
    :return:
    """
    html = requests.get(url)
    ehtml = etree.HTML(html.text)
    urls = ehtml.xpath('//*[@id="js_content"]/p/img/@data-src')
    name = ehtml.xpath('//*[@id="activity-name"]')[0].text.strip()
    # print(len(urls))
    # print(urls[0])
    return name, urls


def get_suffix(url):
    """
    获取后缀
    :param url:
    :return:
    """
    pattern = 'wx_fmt=(\w+)'
    data = re.search(pattern, url)
    if data:
        return "png" if data.group(1) == "png" else "jpg"
    else:
        print(url)
        raise Exception("parse re error")


def download_file(url, store_path, filename):
    """
    下载文件
    :param url:
    :param store_path:
    :param filename:
    :return:
    """
    suffix = get_suffix(url)
    filepath = os.path.join(store_path, filename + "." + suffix)
    file_data = requests.get(url, allow_redirects=True).content
    with open(filepath, 'wb') as handler:
        handler.write(file_data)
    print(filename + "下载完成！")


def make_dir(path, name):
    """
    创建文件夹
    :param path:
    :param name:
    :return:
    """
    if not os.path.exists(os.path.join(path, name)):
        os.chdir(path)  # 改变当前工作目录到指定的路径
        os.mkdir(name)


if __name__ == '__main__':
    main_url = "https://mp.weixin.qq.com/s?__biz=MzU3MTcwNDQyNA==&mid=2247487401&idx=1&sn=c8a84aa7aaf150af4691e7af3f9ff965&chksm=fcdd5aaecbaad3b88d8cf751b64c98a1199f6cbba98169ebb1e1f830e236385c1366d5f6659d&scene=178#rd"
    main_store_path = "E:/"
    main_name, main_urls = get_img_urls(main_url)
    print(main_name)
    make_dir(main_store_path, main_name)
    main_store_path = main_store_path + main_name + '/'

    # 多进程
    # p = Pool(5)
    # for i in range(len(main_urls)):
    #     p = threading.Thread(target=download_file, args=(main_urls[i], main_store_path, str(i + 1).zfill(3)))
    #     p.start()
    # p.join()

    # 多线程
    with ThreadPoolExecutor(max_workers=5) as t:
        obj_list = []
        for i in range(len(main_urls)):
            obj = t.submit(download_file, main_urls[i], main_store_path, str(i + 1).zfill(3))
        for future in as_completed(obj_list):
            future.result()

    # download_file("https://mmbiz.qpic.cn/mmbiz_png/HfLRct59EVy2OrsTR0SepbLERKlwtootFXQ4Ayibyia3NPVUJARApul4ibwv3E2ibUeaRTEFmNExhfppoC2Jaumpzg/640?wx_fmt=png","E:/","001")
