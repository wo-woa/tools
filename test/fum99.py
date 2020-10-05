import requests
import re
from lxml import etree
import time

# 获取论坛所有作品名字生产csv来查找（论坛查找需要vip）
class fum99():
    def __init__(self, url, name):
        self.url = url
        self.name = name
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
        }

    def get_content(self, url):
        try:
            data = requests.get(url, headers=self.headers)
            html = etree.HTML(data.text)
            header_list = html.xpath('//tbody/tr/th/a[2]')
            type_list = html.xpath('//tbody/tr/th/em/a')
            content_list = []
            for i in range(len(header_list)):
                href = str(header_list[i].xpath('./@href')[0])
                tid = re.search("tid=(\d+)", href).group(1)
                content_list.append({"tid": tid, "content": type_list[i].text + ',' +
                                                            header_list[i].text + ',http://fum99.com/' + href})
            return content_list
        except Exception as err:
            print(err)

    def run(self, page):
        s = set()
        flag = 1
        try:
            with open(self.name + '.csv', 'a', encoding='utf-8') as file:
                for i in range(page):
                    content = self.get_content(self.url + '&page=' + str(i + 1))
                    for each in content:
                        if not each["tid"] in s:
                            file.write(each["content"] + '\n')
                            s.add(each["tid"])
                        else:
                            flag = 0
                    if flag == 1:
                        print('成功添加' + str(len(content)) + '行')
                        time.sleep(1)
                    else:
                        print('添加完成')
                        break
        except Exception as err:
            print('run')
            print(err)

    def run2(self, page):
        try:
            with open(self.name + '.csv', 'a', encoding='utf-8') as file:
                for i in range(page):
                    content = self.get_content(self.url + str(i + 1) + '.html')
                    for each in content:
                        file.write(each + '\n')
                    print('成功添加' + str(len(content)) + '行')
        except Exception as err:
            print('run')
            print(err)


# url='https://www.51fuman.com/forum-46-1.html'
url = 'https://www.51fuman.com/forum.php?mod=forumdisplay&fid=46&filter=typeid&typeid=79'

name = 'sr'
a = fum99(url, name)
a.run(1000)
