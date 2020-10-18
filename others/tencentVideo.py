import requests
import json
import re

"""
    https://www.52pojie.cn/thread-1032509-1-1.html
    如果链接是这种类型的https://v.qq.com/x/page/k3003hvljno.html 解析出来的就是完整视频
    如果是这样的https://v.qq.com/x/cover/mzc00200r4zm1zo/w3000j0wzd9.html 就需要获取vid
    方法是进入该页面后查看源码，搜索LIST_INFO
"""
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}


def qq_video(url):
    appver = '3.2.19.333'
    try:
        vid = url.split('/')[-1].split('.')[0]
    except Exception:
        vid = url
    # print(vid)
    url = 'http://vv.video.qq.com/getinfo?otype=json&platform=11&defnpayver=1&appver=' + appver + '&defn=fhd&vid=' + vid
    html = requests.get(url, headers=headers)
    html_text = html.text
    # print(html.text)
    jsonstr = re.findall('QZOutputJson=(.+);$', html_text, re.S)[0]
    # print(jsonstr)
    json_data = json.loads(jsonstr)
    fvkey = json_data['vl']['vi'][0]['fvkey']
    keyid = json_data['vl']['vi'][0]['cl']['ci'][0]['keyid'].split(".")
    filename = keyid[0] + ".p" + keyid[1][2:] + "." + keyid[2] + ".mp4"
    cdn = json_data['vl']['vi'][0]['ul']['ui'][3]['url']
    downloadurl = cdn + filename + "?vkey=" + fvkey + "?type=mp4"
    print("DownloadUrl:" + downloadurl)


if __name__ == "__main__":
    # https://v.qq.com/x/page/k3003hvljno.html
    main_url = input("Put:")
    qq_video(main_url)
