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
                print(link.group())
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


# url='www.fumankong.com'

main_url = 'https://www.fumankong.cc//mobcent/app/web/index.php?r=forum/postlist'
main_date = 'packageName=com.appbyme.app301097&forumType=7&pageSize=10&accessToken=9d22238f6cd72830787d5eb4ef15b' \
            '&appName=%E8%85%90%E6%BC%AB%E6%8E%A7&topicId={id}&authorId=0&egnVersion=v2103.5' \
            '&accessSecret=e529b666669a538789cdbb5176ca5&sdkVersion=2.5.0.0&imei=99001064700010&apphash=4b2edd7b' \
            '&boardId=88&forumKey=q0PvFAdGj0lwMvKxw6&page=1&platType=1&imsi=460110394206015&sdkType='
# date = 'filterType=&packageName=com.appbyme.app301097&sorts=&sortby=all&isImageList=1&egnVersion=v2103.5' \
#        '&imei=99001064700010&sdkVersipackageName=com.appbyme.app301097&forumType=7&pageSize=10&accessToken=9d22238f6cd72830787d5eb4ef15b&appName=%E8%85%90%E6%BC%AB%E6%8E%A7&topicId={id}&authorId=0&egnVersion=v2103.5&accessSecret=e529b666669a538789cdbb5176ca5&sdkVersion=2.5.0.0&imei=99001064700010&apphash=4b2edd7b&boardId=88&forumKey=q0PvFAdGj0lwMvKxw6&page=1&platType=1&imsi=460110394206015&sdkType=on=2.5.0.0&orderby=all&apphash=4b2edd7b&boardId=88&page=1&imsi=460110394206015' \
#        '&sdkType=&longitude=121.5667724609375&forumType=7&circle=0&pageSize=20' \
#        '&accessToken=9d22238f6cd72830787d5eb4ef15b&appName=%E8%85%90%E6%BC%AB%E6%8E%A7' \
#        '&accessSecret=e529b666669a538789cdbb5176ca5&topOrder=1&sortid=0&latitude=29.82301139831543' \
#        '&forumKey=q0PvFAdGj0lwMvKxw6&platType=1?''
# 获取列表数据
# url = 'https://www.fumankong.com//mobcent/app/web/index.php?r=forum/topiclistex'
# date = 'latitude=29.823081970214844&forumType=7&pageSize=20&forumKey=q0PvFAdGj0lwMvKxw6&sdkType=' \
#        '&imsi=460110210578654&apphash=4b2edd7b&packageName=com.appbyme.app301097&sorts=&egnVersion=v2103.5' \
#        '&longitude=121.56653594970703&appName=%E8%85%90%E6%BC%AB%E6%8E%A7' \
#        '&orderby=all&accessToken=9d22238f6cd72830787d5eb4ef15b&isImageList=1' \
#        '&accessSecret=e529b666669a538789cdbb5176ca5&topOrder=1&sortid=0&boardId=88&imei=861658049819918&sortby=all' \
#        '&sdkVersion=2.5.0.0&page=1&filterType=&circle=0&platType=1'


while True:
    print('请输入id:')
    main_id = input()
    response = requests.post(main_url, main_date.format(id=main_id), headers=headers)
    json_text = response.content.decode(response.apparent_encoding)
    main_password, main_content = get_password(json_text)
    print(main_password)
    if input('问号键详情，其他键跳过:') == '?':
        print(main_content)
    if input('空格键继续，其他键退出:') != ' ':
        break
