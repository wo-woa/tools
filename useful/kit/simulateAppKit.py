# -*- coding: utf-8 -*-
import json
import re
import traceback

import requests

headers = {
    'Host': 'www.fumankong.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/28.0.1500.72 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}
main_url = 'https://www.fumankong.cc//mobcent/app/web/index.php?r=forum/postlist'
main_date = 'packageName=com.appbyme.app301097&forumType=7&pageSize=10&accessToken=9d22238f6cd72830787d5eb4ef15b' \
            '&appName=%E8%85%90%E6%BC%AB%E6%8E%A7&topicId={id}&authorId=0&egnVersion=v2103.5' \
            '&accessSecret=e529b666669a538789cdbb5176ca5&sdkVersion=2.5.0.0&imei=99001064700010&apphash=4b2edd7b' \
            '&boardId=88&forumKey=q0PvFAdGj0lwMvKxw6&page=1&platType=1&imsi=460110394206015&sdkType='


def get_password(str):
    try:
        js = json.loads(str)
        content = js['topic']['content']
        result = ''
        # print(content)
        for each in content:
            link = re.search('https://pan[\w./-]+', each['infor'])
            if each['infor'].find('才能浏览') > 0:
                return '需要付费', content
            if each['infor'].find('查看提取码请回复') > 0:
                return '查看提取码请回复', content
            if link:
                result += link.group() + '\r\n'
            # password=re_pass(each['infor'])
            password = re.search(r'验证码.+?\w+|提取码.+?\w+|密码.+?\w+|\[sell=\d+?,\d+?\].+?\[', each['infor'])
            if password:
                result = result + password.group() + '\n'
        if result != '':
            return result, content
        # 美化输出json中带有中文的
        return json.dumps(content, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
    except Exception as e:
        print(traceback.format_exc())
        print(str)


def re_pass(txt):
    pattern_list = '\[sell=\d+?,\d+?\](.+?)\[|验证码.+?(\w+)|提取码.+?(\w+)|密码.+?(\w+)'
    for pattern in pattern_list.split('|'):
        data = re.search(pattern, txt)
        if data:
            return data.group(1)
    return ''


def simulate_app(url):
    pattern = 'tid=(\d+)'
    data = re.search(pattern, url)
    if data:
        id = data.group(1)
    else:
        return '匹配失败', ''
    response = requests.post(main_url, main_date.format(id=id), headers=headers)
    # print(response.content.decode('gb2312'))
    json_text = response.content.decode(response.apparent_encoding)
    return get_password(json_text)

