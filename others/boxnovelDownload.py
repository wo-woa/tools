# -*- coding: utf-8 -*-

"""
Author: XXM
date: 2020/9/27 22:18
desc: https://www.bilibili.com/read/cv6818681/
"""
import requests
import time
import random
import re
from bs4 import BeautifulSoup

USER_AGENT_LIST = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
]


def get_request_headers():
    # 定义request headers头信息
    headers = {
        'User-Agent': random.choice(USER_AGENT_LIST),
        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng,'
                  ' * / *;q = 0.8, application / signed - exchange;v = b3',
        'Accept - Language': 'en-US, en;q = 0.5',
        'Connection': 'keep - alive',
        'Accept - Encoding': 'gzip, deflate, br',
    }
    return headers


def get_random_ip(ip_list):
    """取IP池里随机IP"""
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('https://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'https': proxy_ip}
    return proxies


def sleep_random(i):
    """随机停止；其实没必要写个函数的hh"""
    if (i % 2 == 0):
        time.sleep(random.randint(2, 4))
    if (i % 5 == 0):
        time.sleep(random.randint(1, 2))
    else:
        time.sleep(random.randint(4, 5))


def get_novel_text(url, i, ip_list):
    """递归函数；保证章节不丢失；最大递归深度为4,仍不成功就将该章节写入error.txt文件中"""
    try:
        global flag
        global text_url
        headers = get_request_headers()
        proxies = get_random_ip(ip_list)
        r = requests.get(url + str(i), headers=headers, proxies=proxies, timeout=(10, 10))
        soup = BeautifulSoup(r.text, 'lxml')
        # 找出class为text-left的div
        novel_list = soup.find('div', {'class': 'text-left'})
        pattern = re.compile('h.')  # 匹配任意h.标签
        title = ''
        if novel_list.find(pattern) != None:
            title = novel_list.find(pattern).get_text().strip()
        print("Character %d gets success" % i)
        # 存储到指定路径的txt文件中,追加写入
        if len(title) != 0:
            """boxnovel它网页格式不太统一...有的title是h标题,有的直接放到p里了"""
            f = open(text_url, 'a+', encoding='utf-8')
            f.write('\n\n\n' + str(title) + '\n\n')
            f.close()
        text = novel_list.find_all('p')
        for i in range(0, len(text)):
            text_copy = text[i].get_text().strip()
            f = open(text_url, 'a+', encoding='utf-8')
            f.write(str(text_copy) + '\n')
            f.close()
        sleep_random(i)
        return 1
    except requests.exceptions.RequestException as e:
        print(e)
        time.sleep(1)
        if flag <= 3:
            flag = flag + 1
            return get_novel_text(url, i, ip_list)
        if flag == 4:
            """最多递归4次,仍不成功就将该章节写入error.txt文件中"""
            print("Charcter %d gets failed" % i)
            s = "Character %d gets failed" % i
            f = open(r'E:\error.txt', 'a+', encoding='utf-8')
            f.write(str(s) + '\n')
            f.close()
            return s


def get_novel(ip_list):
    """爬取文本信息"""
    url = 'https://boxnovel.com/novel/lord-of-the-mysteries-webnovel/chapter-'
    for i in range(1405, 1407):
        """i为章节数"""
        global flag
        flag = 0
        get_novel_text(url, i, ip_list)


if __name__ == "__main__":
    text_url = 'E:\Lord.txt'
    flag = 0
    main_ip_list = []  # ip池需要自己设置,标准形式为IP:PORT,例:111.234.554.144:443
    if len(main_ip_list) != 0:
        get_novel(main_ip_list)
