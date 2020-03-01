# -*- coding: utf-8 -*-

'''
Author: XXM
date: 2020/2/29 22:26
desc: 动物餐厅加密数据批量解密
'''
import execjs
import re

js = execjs.compile('''
const r = require("crypto-js");

const globalKey = "oe6z64vj2TTPa2A7mMdiuy0lTG9c"; // 你的openid
function getEncryptString(e, t, i) {
    i || (i = 100 + Math.floor(900 * Math.random()));
    var o = e + 100 + i,
    a = r.MD5(o + globalKey + t).toString();
    return "t" + (a.charAt(17) + a.charAt(3) + a.charAt(27) + a.charAt(11) + a.charAt(23)) + i + e;
}

function getDecrypeString(e,t){
    var i = e.substring(6, 9), o = e.substring(9), a = parseFloat(o);
    return getEncryptString(a, t, parseInt(i)) == e ? a : 0;
}
''')
with open('e:/test/decode.txt', encoding='utf-8') as file:
    string = file.read()
pattern = '\"([^"]+?)\":\"(t[^"].+?)\"'
result = re.finditer(pattern, string)
for i in result:
    string = string.replace(i.group(2), str(js.call('getDecrypeString', i.group(2), i.group(1))))
print(string)

st = 'memorial_unlock_memorial_'
for i in range(59):
    s = st + str(i + 1)
    print(r'\"' + s + r'\":\"' + str(js.call('getEncryptString', 1)) + r'\",', end='')
