import requests
import re
from lxml import etree

# 获取论坛所有作品名字生产csv来查找（论坛查找需要vip）
class fum99():
    def __init__(self,url,name):
        self.url=url
        self.name=name
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
    def get_content(self,url):
        try:
            data = requests.get(url, headers=self.headers)
            html = etree.HTML(data.text)
            header_list=html.xpath('//tbody/tr/th/a[2]')
            type_list=html.xpath('//tbody/tr/th/em/a')
            content_list=[]
            for i in range(len(header_list)):
                href=header_list[i].xpath('./@href')[0]
                content_list.append(type_list[i].text+','+header_list[i].text+',http://fum99.com/'+str(href))
            return content_list
        except Exception as err:
            print(err)
    def run(self,page):
        try:
            with open(self.name+'.csv', 'a',encoding='utf-8') as file:
                for i in range(page):
                    content=self.get_content(self.url+'&page='+str(i+1))
                    for each in content:
                        file.write(each+'\n')
                    print('成功添加'+str(len(content))+'行')
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

# url='https://www.danmei99.com/forum-44-'
url='https://www.danmei99.com/forum.php?mod=forumdisplay&fid=44&filter=typeid&typeid=69'
name='sr'
a=fum99(url,name)
a.run(29)

