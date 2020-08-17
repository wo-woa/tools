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
    html = requests.get(url)
    ehtml = etree.HTML(html.text)
    urls = ehtml.xpath('//*[@id="js_content"]/p/img/@data-src')
    # print(len(urls))
    # print(urls[0])
    return urls


def get_suffix(url):
    pattern = 'wx_fmt=(\w+)'
    data = re.search(pattern, url)
    if data:
        return "png" if data.group(1) == "png" else "jpg"
    else:
        print(url)
        raise Exception("parse re error")


def download_file(url, store_path, filename):
    suffix = get_suffix(url)
    filepath = os.path.join(store_path, filename + "." + suffix)
    file_data = requests.get(url, allow_redirects=True).content
    with open(filepath, 'wb') as handler:
        handler.write(file_data)
    print(filename + "下载完成！")


if __name__ == '__main__':
    main_url = "https://mp.weixin.qq.com/s/3Vzrstwsb2f6YV1ysAilbQ"
    main_store_path = "E:/1/"
    main_urls = get_img_urls(main_url)
    # p = Pool(5)
    # for i in range(len(main_urls)):
    #     p = threading.Thread(target=download_file, args=(main_urls[i], main_store_path, str(i + 1).zfill(3)))
    #     p.start()
    # p.join()

    with ThreadPoolExecutor(max_workers=5) as t:
        obj_list = []
        for i in range(len(main_urls)):
            obj = t.submit(download_file, main_urls[i], main_store_path, str(i + 1).zfill(3))
        for future in as_completed(obj_list):
            future.result()

    # download_file("https://mmbiz.qpic.cn/mmbiz_png/HfLRct59EVy2OrsTR0SepbLERKlwtootFXQ4Ayibyia3NPVUJARApul4ibwv3E2ibUeaRTEFmNExhfppoC2Jaumpzg/640?wx_fmt=png","E:/","001")
