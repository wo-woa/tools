import os
import pyperclip
import json
import time
import re

#由于无法登陆p站，但是图片地址可以下载，使用手动复制pixiv页面显示作品接口的数据来获取下载地址

# 网站搜索illusts
class pSite():
    def __init__(self, name):
        self.name = name
        self.ids = []
        if os.path.exists(name):
            with open(name, encoding='utf-8') as file:
                while True:
                    line = file.readline()
                    a = line.strip()
                    b=''
                    if a != b:
                        id = line.split(',')[1]
                        self.ids.append(id)
                    else:
                        break

    def add(self, text):
        if (text[0] == '{'):
            txt = json.loads(text)
            with open(self.name, 'a', encoding='utf-8') as csv:
                works = txt['body']['works']
                count = 0
                for each in works:
                    if self.check_id_exist(works[each]['id']):
                        csv.write(self.replace_comma(works[each]['title']) + ',' + str(works[each]['id']) + ','
                                  + works[each]['url'] + ','
                                  + self.replace_comma(str(works[each]['tags'])) + ','
                                  + str(works[each]['width']) + ',' + str(works[each]['height']) + ','
                                  + str(works[each]['pageCount']) + ',' + str(works[each]['xRestrict']) + ','
                                  + str(works[each]['restrict'])
                                  + '\n')
                        self.ids.append(works[each]['id'])
                        count += 1
                print('添加成功' + str(count) + '个')
        else:
            print('格式不符合')

    def check_id_exist(self, id):
        if id in self.ids:
            return False
        else:
            return True

    def replace_comma(self, str):
        return str.replace(',,', '，')

    def show_ids_length(self):
        print(len(self.ids))

    def replace_comma(self, str):
        return str.replace(',', '，')

    def get_img_urls(self):
        if os.path.exists(self.name):
            with open(self.name, encoding='utf-8') as file:
                with open('urls.txt', 'a') as url_text:
                    while True:
                        line = file.readline()
                        if line and line.strip() != '':
                            url = line.split(',')[2]
                            page = line.split(',')[6]
                            urls = self.get_real_urls(url, page)
                            for each in urls:
                                url_text.write(each + '\n')
                        else:
                            break

    def get_real_urls(self, url, page):
        url = url.replace('/c/250x250_80_a2', '')
        url = re.sub('\d(?=_square)', '{page}', url)
        urls = []
        for each in range(int(page)):
            urls.append(url.format(page=str(each)))
        return urls

    def run(self):
        buffer = ''
        while True:
            paste = pyperclip.paste()
            if paste != buffer:
                self.add(paste)
                buffer = paste
            time.sleep(1)


name = 'ross.csv'
qj = pSite(name)
qj.run()
# qj.get_img_urls()

# 缩略图 https://i.pximg.net/c/250x250_80_a2/img-master/img/2015/06/15/22/19/38/50918112_p0_square1200.jpg
# 放大裁剪图 https://i.pximg.net/img-master/img/2015/06/15/22/19/38/50918112_p0_square1200.jpg
# 完整压缩图 https://i.pximg.net/img-master/img/2015/06/15/22/19/38/50918112_p0_master1200.jpg
# 原图 https://i.pximg.net/img-original/img/2017/07/18/10/08/53/50918112_p0.jpg
