# -*- coding: utf-8 -*-

import urllib
import requests
import time
from urllib import parse
import json
from prettytable import PrettyTable
import hashlib
import base64
from urllib import parse
import re

header = {
    "Content-Type": "application/x-www-form-urlencoded"
}


def get_book_list(name):
    url = 'http://read.xiaoshuo1-sm.com/novel/i.php?do=is_search&q={name}&p=1&page=1&size=10'
    name = parse.quote(name)
    url = url.format(name=name)
    data = requests.get(url)
    if data.status_code != 200:
        raise Exception('invalid url')
    js = json.loads(data.text)
    data_list = []
    buffer = []
    for each in append:
        buffer.append(js['aladdin'][each])
    data_list.append(buffer)
    for each in js['data']:
        buffer = []
        for i in append:
            buffer.append(each[i])
        data_list.append(buffer)
    return data_list


def pretty_table(data):
    table = PrettyTable(append_name)
    for each in data:
        table.add_row(each)
    print(table)


def get_md5_value(src):
    myMd5 = hashlib.md5()
    myMd5.update(src.encode('utf-8'))
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest


def download_text(id):
    data = id + '1514984538213800000037e81a9d8f02596e1b895d07c171d5c9'
    url = 'http://walden1.shuqireader.com/webapi/book/chapterlist'
    md5 = get_md5_value(data)
    post_data = 'timestamp=1514984538213&user_id=8000000&bookId=' + id + '&sign=' + md5
    web_data = requests.post(url, data=post_data, headers=header)
    js = json.loads(web_data.text)
    print('开始下载小说：' + js['data']['bookName'] + ',作者：' + js['data']['authorName'])
    print('一共有' + str(len(js['data']['chapterList'])) + '卷')
    with open(js['data']['bookName']+'.txt','w+') as file:
        for num1, each1 in enumerate(js['data']['chapterList']):
            print('开始下载第' + str(num1 + 1) + '卷')
            print('一共有' + str(len(each1['volumeList'])) + '章')
            for each2 in each1['volumeList']:
                print(each2['chapterName'] + '开始下载')
                text=get_chapter_content(id,each2['chapterId'])
                file.write(each2['chapterName']+'\n'+text+'\n\n\n')
            file.flush()
    input('下载完成，按任意键退出')


def get_chapter_content(book_id, chapter_id):
    url = 'http://c1.shuqireader.com/httpserver/filecache/get_book_content_{book}_{chapter}_1463557822_1_0.xml'
    url = url.format(book=book_id, chapter=chapter_id)
    data = requests.get(url)
    pattern = 'CDATA\[(.+)\]\]'
    re_data = re.search(pattern, data.text)
    if re_data:
        content = re_data.group(1)
        return decrypt(content)
    else:
        raise Exception('not match')


def decrypt(txt):
    real_txt = b''
    for count, word in enumerate(txt):
        if 'A' <= word and word <= 'Z':
            word_count = ord(word) + 13
            if word_count > 90:
                word_count = word_count % 90 + 64
            word = chr(word_count)
        elif 'a' <= word and word <= 'z':
            word_count = ord(word) + 13
            if word_count > 122:
                word_count = word_count % 122 + 96
            word = chr(word_count)
        real_txt = real_txt + bytes(word, encoding="utf8")

    real_txt = real_txt.decode('utf-8')
    real_txt = base64.b64decode(real_txt)
    real_txt = real_txt.decode('utf-8')
    real_txt = real_txt.replace('<br/>　', '\n')
    return real_txt


append = ['title', 'author', 'category', 'tags', 'hh_hot', 'words', 'bid']
append_name = ['名字', '作者', '分类', '标签', '热度', '字数', 'id']
name = '最强总裁'



data = get_book_list(name)
pretty_table(data)
num=input('请选择下载的书籍')
id=data[int(num)-1][6]
print(id)
download_text(id)

# print(get_chapter_content('4590110', '341763'))
# download_text('7105436')

# "sid": "6290180e24bfc50745cef035a6d55fde",
# "title": "不朽神帝",
# "author": "揭家胖子",
# "category": "东方玄幻",
# "tags": "热血,重生,争霸流,小说",
# "hh_hot": 101,
# "words": 424739,
# "host": "shuqi.com",
# "base": 0,
# "bid": 6800964,
# "mgbid": 0,
# "authorid": 3602598,
# "status": 1,
# "limitFree": 0,
# "limitFreeEnd": 0,
# "isMonthly": 0,
# "monthlyEnd": 0,
# "top_class": "502",
# "formats": 1,
# "first_cid": 678926,
# "first_chapter": "第1章十万年后",
# "cover": "http://img-tailor.11222.cn/bcv/big/201608161407582806.jpg",
# "desc": "十万年前，神武灵三道争雄，武皇之子叶少龙遭灵道暗算，陨落万界山！十万年后，武道彻底没落。叶少龙重生于古苍州玄剑宗一个杂役弟子身上！重生一世，叶少龙注定要辉煌崛起，剑斩天才，重领武道巅峰！?待我重修一世，天地阴阳逆乱！以我热血洒满诸天，天下共尊不朽神帝！",
# "second_category_name": "东方玄幻",
# "first_category_name": "玄幻",
# "second_category_id": "2",
# "first_category_id": "1",
# "audioPlayCount": "18688",
# "quansouAlbumId": ""
