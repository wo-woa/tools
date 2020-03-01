from lxml import etree
import requests
import re
import codecs

#获取ita5网站的书籍生成txt文件

class CrawlText():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }

    def get_firstpage_info(self, url):
        data = requests.get(url, headers=self.headers)
        html = etree.HTML(data.text)
        text_list = html.xpath('//*[@id="read_tpc"]/p')
        self.name = self.get_name(html)
        self.page = self.get_page_count(html)
        text = ''
        for each in text_list:
            if isinstance(each.text, str):
                text = text + each.text + '\n'
        if text is not None:
            print('正在处理第1页')
            return text
        else:
            raise Exception('文本获取失败')

    def get_page_text(self, url):
        count = 0
        try:
            data = requests.get(url, headers=self.headers)
            html = etree.HTML(data.text)
            text_list = html.xpath('//*[@id="read_tpc"]/p')
            # 除了第一页，之后首行的文本匹配规则不同
            text = html.xpath('//*[@id="read_tpc"]/text()')[0].strip() + '\n'
            for each in text_list:
                if isinstance(each.text, str):
                    text = text + each.text + '\n'
            if text is not None:
                return text
            else:
                print('文本获取失败')
                raise Exception('文本获取失败')
        except Exception as err:
            # 有时候莫名其妙出错，重试即可，很少
            if count < 3:
                print('获取失败重新尝试第' + str(count + 1) + '次......')
                return self.get_page_text(url)
            else:
                print('\033[1;31m 当前页有问题\033[0m \n')

    def get_page_count(self, html):
        page_list = html.xpath('//*[@id="view_article"]//td[@class="page"]/a/@href')
        href = page_list[-1]
        page = re.search('page-(\d+)\.', href)
        if page:
            print('一共有' + page.group(1) + '页')
            return page.group(1)
        else:
            raise Exception('页面数获取失败')

    def get_name(self, html):
        title = html.xpath('//*[@id="view_article"]//div[@class="main_title"]/text()')[0]
        name = re.search('：(.+?)\(', title)
        if name:
            print('正在处理书籍' + name.group(1))
            return name.group(1)
        else:
            raise Exception('名称获取失败')

    def run(self, url):
        text = self.get_firstpage_info(url)
        with codecs.open(self.name + '.txt', 'w', 'utf_8_sig') as file:
            file.write(text)
            for i in range(2, int(self.page) + 1):
                print('正在处理第' + str(i) + '页')
                last_url = url.replace('-id', '-aid').replace('.html', '-page-' + str(i) + '.html')
                text = self.get_page_text(last_url)
                file.write(text)


url = 'http://www.ita5.com/news/bencandy-htm-fid-50-id-8634.html'
c = CrawlText()
c.run(url)
# txt=c.get_page_text('http://www.ita5.com/news/bencandy-htm-fid-3-aid-7674-page-52.html')
# print(txt)
print('success.......')
