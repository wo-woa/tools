import json
import re
import requests

headers = {
    'Host': 'www.fumankong.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}


def get_password(str):
    
    js = json.loads(str)
    content = js['topic']['content']
    for each in content:
        link = re.search('https://[\w./-]+', each['infor'])
        if each['infor'].find('才能浏览')>0:
            return '需要付费'
        if each['infor'].find('查看提取码请回复')>0:
            return '查看提取码请回复'
        if link:
            print(link.group())
        result = re.search('验证码：\w+|提取码.\w+|密码[:：]\w+|\[sell=\d+?,\d+?\][A-Za-z0-9_]+', each['infor'])
        if result:
            return result.group()
    return str


# url='www.fumankong.com'
url = 'https://www.fumankong.com//mobcent/app/web/index.php?r=forum/postlist'
date = 'packageName=com.appbyme.app301097&forumType=7&pageSize=10&accessToken=e8576268548d8c3ed48ea959225d5&appName=%E8%85%90%E6%BC%AB%E6%8E%A7&topicId={id}&authorId=0&egnVersion=v2103.5&accessSecret=29d3743008928d453836f122b008a&sdkVersion=2.5.0.0&imei=99001064700010&apphash=ddf6b0a4&boardId=88&forumKey=q0PvFAdGj0lwMvKxw6&page=1&platType=1&imsi=460110210578654&sdkType='
# id=146951
print('请输入id')
id = input()

response = requests.post(url, date.format(id=id), headers=headers)
# print(response.content.decode('gb2312'))
json_text = response.content.decode(response.apparent_encoding)
print(get_password(json_text))
input('运行完成，按任意键退出')
