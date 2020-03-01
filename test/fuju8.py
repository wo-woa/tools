# -*- coding: utf-8 -*-

import urllib
import requests
import time

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "125",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "HmEW_2132_saltkey=K8t0d8pq; HmEW_2132_lastvisit=1547975036; "
              "UM_distinctid=1686ab78b3143a-0b503803a8bed7-b781636-144000-1686ab78b32b0e; "
              "CNZZDATA1274069092=1107480614-1547978528-https%253A%252F%252Fwww.baidu.com%252F%7C1547978528; "
              "Hm_lvt_53cf16f083388d7f7dd87d3af5f10a00=1547978641; HmEW_2132_seccode=425.a4e0d837a64e2f5f0b; "
              "HmEW_2132_ulastactivity=a1a5EznvmKDHyppiiDJ51wOmsJ%2FjDwqXdblg8byjx7TKKTmTdOK9; "
              "HmEW_2132_auth=ee05zww8NTdazSbvDvJYK6xkZ2s69iHblMeFLFODrS41nxGknlss51a5ehHHLJXwORapC4v2a%2FzMxDC"
              "HU7xxGiTJGQ; HmEW_2132_smile=5D1; HmEW_2132_nofavfid=1; HmEW_2132_study_nge_extstyle=2; "
              "HmEW_2132_study_nge_extstyle_default=2; HmEW_2132_home_diymode=1; HmEW_2132_editormode_e=1; "
              "HmEW_2132_visitedfid=49D50D51D40D42; HmEW_2132_viewid=tid_10004; "
              "HmEW_2132_st_t=10221%7C1547981779%7Cf037dd1b60817e1cc890b938f053fb56; "
              "HmEW_2132_forum_lastvisit=D_40_1547978814D_49_1547981779; HmEW_2132_sid=dm303f; "
              "HmEW_2132_lip=125.111.196.103%2C1547981779; HmEW_2132_sendmail=1; HmEW_2132_noticeTitle=1; "
              "HmEW_2132_st_p=10221%7C1547982991%7Cec79c30bc977030bbc2640cf634ea3eb; "
              "Hm_lpvt_53cf16f083388d7f7dd87d3af5f10a00=1547982996; "
              "HmEW_2132_lastact=1547983032%09forum.php%09ajax",
    "Host": "www.fuju8.com",
    "Origin": "http://www.fuju8.com",
    "Referer": "http://www.fuju8.com/thread-10004-2-1.html",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
url = 'http://www.fuju8.com/forum.php?mod=post&action=reply&fid=49&tid=12020extra=page' \
      '%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1'
postdata = 'message=%BD%F0%B1%D2%BD%F0%B1%D2%BD%F0%B1%D2%BD%F0%B1%D2%BD%F0%B1%D2&posttime=1547979489&formhash=14c0125e&usesig=&subject=++'
i=9
while (i):
    data = requests.post(url, data=postdata, headers=header)
    if (data.text.find('回复发布成功')):
        print('success')
    else:
        print(data.text)
        break
    time.sleep(16)
    i=i-1
