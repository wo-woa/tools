# -*- coding: utf-8 -*-

import urllib
import urllib.request
import http.cookiejar
import json
import xlwt

email = '318844856@qq.com'
pwd = 'zxcvbnm'
data = {'email':email,'raw_pwd': pwd}
post_data = urllib.parse.urlencode(data).encode(encoding='UTF8')

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

response = opener.open('http://www.baicizhan.com/login', post_data)
# # print(response .read())
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
row=0
for i in range(1, 60):
    content = json.loads(opener.open("http://www.baicizhan.com/user/all_done_words_list?page=%s"%i).read())
    for word in content["list"]:
        ws.write(row, 0, word["wrong_times"])
        ws.write(row, 1, word["word"])
        ws.write(row, 2, word["word_meaning"].strip())
        row+=1

wb.save('example.xls')
