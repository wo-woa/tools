# -*- coding: utf-8 -*-

"""
Author: XXM
date: 2020/9/19 20:09
desc: 
"""
import json
import requests
import re
import execjs

headers = {
    ":authority": "ac.qq.com",
    ":method": "GET",
    ":path": "/ComicView/index/id/531490/cid/1",
    ":scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "cookie": "__AC__=1; pgv_pvi=316778496; RK=ZYAsHtHcYs; ptcz=42c9b739ab63eeef907b63bfccd84b5db5b4726a40f5219035cdb5701aeb24f3; pgv_pvid=4724830328; tvfe_boss_uuid=5fad3b14a53016d3; pac_uid=0_5d7dfa247d947; eas_sid=H1H5b8Q7a8x2w0N3k7a8L0V3o5; XWINDEXGREY=0; iip=0; uin=o0318844856; skey=@JvN3debOz; theme=white; roastState=2; readRecord=%5B%5B531490%2C%22%E4%B8%80%E4%BA%BA%E4%B9%8B%E4%B8%8B%22%2C1%2C%221.%E5%A7%90%E5%A7%901%22%2C1%5D%5D; readLastRecord=%5B%5D; pgv_info=ssid=s3439161960; ts_uid=8424363729; Hm_lvt_f179d8d1a7d9619f10734edb75d482c4=1600516841; nav_userinfo_cookie=; ac_wx_user=; ts_last=ac.qq.com/ComicView/index/id/531490/cid/1; Hm_lpvt_f179d8d1a7d9619f10734edb75d482c4=1600527114",
    "referer": "https://ac.qq.com/Comic/comicInfo/id/531490",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
}


def getdata():
    url = 'https://ac.qq.com/ComicView/index/id/531490/cid/1'
    response = requests.get(url).text
    data = re.findall("(?<=var DATA = ').*?(?=')", response)[0]
    nonce = re.findall('window\[".+?(?<=;)', response)[0]
    nonce = '='.join(nonce.split('=')[1:])[:-1]
    # print(data)
    # print(nonce)
    nonce = eval(nonce)
    T = list(data)
    N = re.findall('\d+[a-zA-Z]+', nonce)
    jlen = len(N)
    while jlen:
        jlen -= 1
        jlocate = int(re.findall('\d+', N[jlen])[0]) & 255
        jstr = re.sub('\d+', '', N[jlen])
        del T[jlocate:jlocate + len(jstr)]
    T = ''.join(T)
    keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    a = []
    e = 0
    try:
        while e < len(T):
            b = keyStr.index(T[e])
            e += 1
            d = keyStr.index(T[e])
            e += 1
            f = keyStr.index(T[e])
            e += 1
            g = keyStr.index(T[e])
            e += 1
            b = b << 2 | d >> 4
            d = (d & 15) << 4 | f >> 2
            h = (f & 3) << 6 | g
            a.append(b)
            if 64 != f:
                a.append(d)
            if 64 != g:
                a.append(h)
    except:
        print(e)
        print(len(T))
    print(bytes(a))
    _v = json.loads(bytes(a))
    print(_v)


def getdata2():
    import requests
    import re
    import execjs
    import json
    url = 'https://ac.qq.com/ComicView/index/id/531490/cid/1'
    while True:
        try:
            response = requests.get(url).text
            data = re.findall("(?<=var DATA = ').*?(?=')", response)[0]
            # nonce = re.findall('window\[".+?(?<=;)', response)[0]
            # nonce = '='.join(nonce.split('=')[1:])[:-1]
            # nonce = execjs.eval(nonce)
            pattern = 'window\["nonc"\+"e"\] = (.+?);'
            r = re.search(pattern, response)
            nonce = r.group(1)
            nonce = execjs.eval(nonce)
            break
        except:
            pass
    T = list(data)
    N = re.findall('\d+[a-zA-Z]+', nonce)
    jlen = len(N)
    while jlen:
        jlen -= 1
        jlocate = int(re.findall('\d+', N[jlen])[0]) & 255
        jstr = re.sub('\d+', '', N[jlen])
        del T[jlocate:jlocate + len(jstr)]
    T = ''.join(T)
    keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    a = []
    e = 0
    print(len(T))
    while e < len(T):
        b = keyStr.index(T[e])
        e += 1
        d = keyStr.index(T[e])
        e += 1
        f = keyStr.index(T[e])
        e += 1
        g = keyStr.index(T[e])
        e += 1
        b = b << 2 | d >> 4
        d = (d & 15) << 4 | f >> 2
        h = (f & 3) << 6 | g
        a.append(b)
        if 64 != f:
            a.append(d)
        if 64 != g:
            a.append(h)
    _v = json.loads(bytes(a))
    print(_v)


main_js = """function Base() {
    _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    this.decode = function(c) {
        var a = "",
        b, d, h, f, g, e = 0;
        for (c = c.replace(/[^A-Za-z0-9\+\/\=]/g, ""); e < c.length;) b = _keyStr.indexOf(c.charAt(e++)),
        d = _keyStr.indexOf(c.charAt(e++)),
        f = _keyStr.indexOf(c.charAt(e++)),
        g = _keyStr.indexOf(c.charAt(e++)),
        b = b << 2 | d >> 4,
        d = (d & 15) << 4 | f >> 2,
        h = (f & 3) << 6 | g,
        a += String.fromCharCode(b),
        64 != f && (a += String.fromCharCode(d)),
        64 != g && (a += String.fromCharCode(h));
        return a = _utf8_decode(a)
    };
    _utf8_decode = function(c) {
        for (var a = "",
        b = 0,
        d = c1 = c2 = 0; b < c.length;) d = c.charCodeAt(b),
        128 > d ? (a += String.fromCharCode(d), b++) : 191 < d && 224 > d ? (c2 = c.charCodeAt(b + 1), a += String.fromCharCode((d & 31) << 6 | c2 & 63), b += 2) : (c2 = c.charCodeAt(b + 1), c3 = c.charCodeAt(b + 2), a += String.fromCharCode((d & 15) << 12 | (c2 & 63) << 6 | c3 & 63), b += 3);
        return a
    }
}
function  calc(T,N){
	var B = new Base(),
	T = T.split(''),
	N = N.match(/\d+[a-zA-Z]+/g);
	len = N.length;
	while (len--) {
		locate = parseInt(N[len]) & 255;
		str = N[len].replace(/\d+/g, '');
		T.splice(locate, str.length)
	}
	T = T.join('');
	_v = JSON.parse(B.decode(T));
	return _v;
}
"""


def get_data():
    url = 'https://ac.qq.com/ComicView/index/id/531490/cid/1'
    response = requests.get(url).text
    data = re.findall("(?<=var DATA = ').*?(?=')", response)[0]
    nonce = re.findall('window\[".+?(?<=;)', response)[0]
    nonce = '='.join(nonce.split('=')[1:])[:-1]
    nonce = eval(nonce)
    print(data)
    print(nonce)
    js = execjs.compile(main_js)
    result = js.call('calc', data, nonce)
    print(result)


main_m = "edbecfayJdjba21pYyI6eyJpefZCI6NTMxNDkwLCJ0aaXRsZSI6Ilx1NGUwMFx1NGViYVx1NGU0Ylx1NGUwYiIsImNvebGxlY3QiOiI1MjcyMzgyIiwiaXNKYXBhbkNvbWljIjbpmYWxzZSwiaXNMaWdodE5vdmVsIjpmYWxzZSwiaXNMaWdodENvbWljIjpmYWxzZSwiaXNGaW5pc2giOmZhbHNlLCJpc1JvYXN0YWJsZSI6dHJ1ZSwiZUlkIjoiS2xCTVNFTkNWMU5WQXdNZkFRWUhBd0VKSEVFeSJ9LCJjaGFwdGVyIjp7ImNpZCI6MSwiY1RpdGxlIjoiMS5cdTU5ZDBcdTU5ZDAxIiwiY1NlcSI6IjEiLCJ2aXBTdGF0dXMiOjEsInByZXZDaWQiOjAsIm5leHRDaWQiOjIsImJsYW5rRmlyc3QiOjEsInZfY2x1Yl9zdGF0ZSI6IjEiLCJpc19hcHBfY2hhcHRlciI6ZmFsc2UsImNhblJlYWQiOnRydWV9LCJwaWN0dXJlIjpbeyJwaWQiOiIzMzIwMSIsIndpZHRoIjoxMjAwLCJoZWlnaHQiOjE5MDcsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMDhfMTJfNTlfYTYyZTk2ZDUxYmFiMmMxYWI0MGVkN2ZmNjU4OGY1NjUyXzExMjM3MTY4Ny5qcGdcLzAifSx7InBpZCI6Ijc3ODgiLCJ3aWR0aCI6ODAwLCJoZWlnaHQiOjEyNzAsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMTZfMTJfNTVfNGY5YzczMzIzOWI1ZjM4MTZmMjEyN2RlY2E5ZWY2ZjdfNzc4OC5qcGdcLzAifSx7InBpZCI6Ijc3ODkiLCJ3aWR0aCI6ODAwLCJoZWlnaHQiOjEyNzAsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMTZfMTJfNTVfY2U5YjM2YmM2MGUxNjFiNjRjNzI5MTA3YzI2OTEwOTVfNzc4OS5qcGdcLzAifSx7InBpZCI6Ijc3OTAiLCJ3aWR0aCI6ODAwLCJoZWlnaHQiOjEyNzAsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMTZfMTJfNTZfMjBmOWU0NWM5Zjk5NzBmNGNkMWJhYzc1NWI4MGNiNGZfNzc5MC5qcGdcLzAifSx7InBpZCI6Ijc3OTEiLCJ3aWR0aCI6ODAwLCJoZWlnaHQiOjEyNzAsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMTZfMTJfNTZfYTM0ODEyNGUyYzBlZTJkYjg5NTVmOWI4YTNhYjVkODhfNzc5MS5qcGdcLzAifSx7InBpZCI6Ijc3OTIiLCJ3aWR0aCI6ODAwLCJoZWlnaHQiOjEyNzAsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMTZfMTJfNTZfNzAyOWU5MjU4NTI3M2MzNzMwN2MyZTE5Mjk0OTEwNzdfNzc5Mi5qcGdcLzAifSx7InBpZCI6Ijc3OTMiLCJ3aWR0aCI6ODAwLCJoZWlnaHQiOjEyNzAsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMTZfMTJfNTZfMDUwNDAxYjdlNjMyNDFhODhhMjYwYzgxM2FlODIzNGZfNzc5My5qcGdcLzAifSx7InBpZCI6Ijc3OTQiLCJ3aWR0aCI6ODAwLCJoZWlnaHQiOjEyNzAsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMTZfMTJfNTZfZmYzMzNhNWRmYTA1NzdmMTExODE1ZDFiODVjMzdhM2NfNzc5NC5qcGdcLzAifSx7InBpZCI6Ijc3OTUiLCJ3aWR0aCI6ODAwLCJoZWlnaHQiOjEyNzAsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMTZfMTJfNTZfNDVhYTAwMTAyYTVjNzk0Yzg2ZWY1MDE3YzFhNDZkYWNfNzc5NS5qcGdcLzAifSx7InBpZCI6Ijc3OTYiLCJ3aWR0aCI6ODAwLCJoZWlnaHQiOjEyNzAsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMTZfMTJfNTZfNzZhNDI0MjM4NTUwNmZhMDE3MGY5M2E2YWNhYWQwMWRfNzc5Ni5qcGdcLzAifSx7InBpZCI6Ijc3OTciLCJ3aWR0aCI6ODAwLCJoZWlnaHQiOjEyNzAsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMTZfMTJfNTZfZGNlMGM3YjU4NWQyMDhlNjY0Y2JhMjg1MDEzM2EwZWRfNzc5Ny5qcGdcLzAifSx7InBpZCI6Ijc3OTgiLCJ3aWR0aCI6ODAwLCJoZWlnaHQiOjEyNzAsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMTZfMTJfNTZfMGQ1NWUyOTFiZjgwMDU2YWRhMmZjYWU3N2ExMGE5ZTVfNzc5OC5qcGdcLzAifSx7InBpZCI6Ijc3OTkiLCJ3aWR0aCI6ODAwLCJoZWlnaHQiOjEyNzAsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMTZfMTJfNTZfYzhhZDNkMzI2OGYyMGVlNDU5YzU3NGU1NDRmYjQxMzVfNzc5OS5qcGdcLzAifSx7InBpZCI6Ijc4MDAiLCJ3aWR0aCI6ODAwLCJoZWlnaHQiOjEyNzAsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMTZfMTJfNTZfMjBkZTExNWNkZTNhYzlmOTJlMjc0MWQ0MzY3OWM4N2NfNzgwMC5qcGdcLzAifSx7InBpZCI6Ijc4MDEiLCJ3aWR0aCI6ODAwLCJoZWlnaHQiOjEyNzEsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMTZfMTJfNTZfNzBmMmEwNDE3NTViNjc2ODcwNjNmMzJlMTJlN2NkMWRfNzgwMS5qcGdcLzAifSx7InBpZCI6Ijc4MDIiLCJ3aWR0aCI6ODAwLCJoZWlnaHQiOjEyNzAsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMTZfMTJfNTZfYzQxZWI2M2JiNTZmNTRhNDcyMzk4ZjhlYjBlZGE4MmNfNzgwMi5qcGdcLzAifSx7InBpZCI6Ijc4MDMiLCJ3aWR0aCI6ODAwLCJoZWlnaHQiOjEyNzAsInVybCI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvbWFuaHVhX2RldGFpbFwvMFwvMTZfMTJfNTZfOTVlMzVlM2FiMGQ2OWY2NTk0NTMyZjA3NDAzZmYyZGZfNzgwMy5qcGdcLzAifV0sImFkcyI6eyJ0b3AiOnsidGl0bGUiOiJcdTUxNmNcdTc2Y2EiLCJ1cmwiOiJodHRwczpcL1wvd2VpYm8uY29tXC81NjE2NTQ5MzY5XC9KamNKNWI1aTU/ZnJvbT1wYWdlXzEwMDIwNjU2MTY1NDkzNjlfcHJvZmlsZSZ3dnI9NiZtb2Q9d2VpYm90aW1lJnR5cGU9Y29tbWVudCNfcm5kMTU5OTUzNDY0NTIwNSIsInBpYyI6Imh0dHBzOlwvXC9tYW5odWEucXBpYy5jblwvb3BlcmF0aW9uXC8wXC8wOF8xMV8yNV82MTk2ODNjMDYyNGNjNjhkYjExYmVjZTVhNzA2ZmYzOV8xNTk5NTM1NTUxNzMxLmpwZ1wvMCJ9LCJib3R0b20iOiIifSwiYXJ0aXN0Ijp7ImF2YXRhciI6Imh0dHBzOlwvXC9cL3EzLnFsb2dvLmNuXC9nP2I9cXEmaz01aHZlUkRSRGNxenZVeURFSE95TnFnJnM9MTAwJnQ9MTQ5NzcwMTk2NSIsIm5pY2siOiJcdTUyYThcdTZmMmJcdTU4MDJcdTVjMGZcdTRlZDkiLCJ1aW5DcnlwdCI6Ik1YZzFVRUZFY0RaS1lqWnBjSEZqYnl0ellrbG5kejA5In19"
main_n = '1d6a2becfa87e642b6679f40a23e9d87'


def test():
    data = main_m
    nonce = main_n
    T = list(data)
    N = re.findall('\d+[a-zA-Z]+', nonce)
    jlen = len(N)
    while jlen:
        jlen -= 1
        jlocate = int(re.findall('\d+', N[jlen])[0]) & 255
        jstr = re.sub('\d+', '', N[jlen])
        del T[jlocate:jlocate + len(jstr)]
    T = ''.join(T)
    keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    a = []
    e = 0
    print(len(T))
    while e < len(T):
        b = keyStr.index(T[e])
        e += 1
        d = keyStr.index(T[e])
        e += 1
        f = keyStr.index(T[e])
        e += 1
        g = keyStr.index(T[e])
        e += 1
        b = b << 2 | d >> 4
        d = (d & 15) << 4 | f >> 2
        h = (f & 3) << 6 | g
        a.append(b)
        if 64 != f:
            a.append(d)
        if 64 != g:
            a.append(h)
    _v = json.loads(bytes(a))
    print(_v)


if __name__ == '__main__':
    # get_data()
    getdata2()
    # test()
