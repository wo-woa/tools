# coding:utf8
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing
import requests, os, codecs, time
from lxml import etree

url = 'https://www.biquge5200.cc/100_100533/'  # 要下载的小说章节列表页面url


def getsource(url):
    try:
        s = requests.get(url)
    except:
        print('访问异常，跳过~！')
    else:
        s.encoding = 'gbk'
        return s.text


def getlist(url):
    global txtname, txtzz
    html = getsource(url)
    ehtml = etree.HTML(html)
    u = ehtml.xpath('//*[@id="list"]/dl/dd/a/@href')
    t = ehtml.xpath('//*[@id="list"]/dl/dd/a/text()')
    txtname = ehtml.xpath('//*[@id="info"]/h1/text()')[0].replace('\\', '').replace('/', '').replace(':', '').replace(
        '*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
    txtzz = ehtml.xpath('//*[@id="info"]/p[1]/text()')[0].replace('\xa0', '')
    num = 0
    for i in range(9, len(u)):
        urllist.append(u[i] + '|' + t[i] + '|' + str(num))
        num += 1


def downtxt(url):
    global downcount
    u = url.split('|')[0]
    t = url.split('|')[1]
    num = url.split('|')[2]
    content = ''
    while len(content) == 0:
        html = getsource(u)
        try:
            ehtml = etree.HTML(html)
        except:
            print(html)
        content = ehtml.xpath('string(//*[@id="content"])').replace('    ', '\r\n').replace('　　', '\r\n').replace(
            '\xa0', '').replace('\ufffd', '').replace('\u266a', '').replace('readx;', '')
    if os.path.exists(savepath + num + '.txt'):
        print(num + '.txt 已经存在!')
    else:
        with codecs.open(savepath + num + '.txt', 'a')as f:
            f.write('\r\n' + t + '\r\n' + content)
        print(t + ' 下载完成!')
        downcount += 1


time_start = time.time()
downcount = 0
urllist = []
getlist(url)
savepath = os.getcwd() + '\\' + txtname + '\\'
if os.path.exists(savepath) == False:
    os.makedirs(savepath)
pool = ThreadPool(multiprocessing.cpu_count())
results = pool.map(downtxt, urllist)
pool.close()
pool.join()
print('开始合并txt...')
with codecs.open(savepath + txtname + '.txt', 'a')as f:
    f.write(txtname)
    f.write('\r\n')
    f.write(txtzz)
    f.write('\r\n')
    for i in range(0, len(urllist)):
        with open(savepath + str(i) + '.txt', "r") as fr:
            txt = fr.read()
            f.write(txt)
            f.write('===========================')
            fr.close()
            os.remove(savepath + str(i) + '.txt')
print('小说合并完成~！')
print('')
print('*' * 15 + ' 任务完成，结果如下：' + '*' * 15)
print('')
print('<' + txtname + '> 下载完成' + '，获取并下载章节页面：' + str(downcount) + ' 个')
print('')
print('耗时：' + str(time.time() - time_start) + ' s')
print('')
print('*' * 51)
