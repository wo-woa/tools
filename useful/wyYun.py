# -*- coding: utf-8 -*-

"""
Author: XXM
date: 2020/9/5 20:39
desc: 
"""
import requests
from requests.cookies import RequestsCookieJar
from lxml import etree

headers = {
    'cookie': '_ntes_nuid=0070f07d2b05c161a823c9e7ebb53e23; ntes_kaola_ad=1; vinfo_n_f_l_n3=9d18fd6ba2029f70.1.2.15716'
              '75448202.1574869499266.1580289105950; WM_TID=+tu0kp6spdhFVAUBAEZ7AUhZtI6IERIA; _ntes_nnid=0070f07d2b05c1'
              '61a823c9e7ebb53e23,1595861573717; _iuqxldmzr_=32; __remember_me=true; WM_NI=XFtuFRNksrLQnssosq5Lh+wwDZH5'
              'xr2BkAoyO76Kj1VMOEG575ki17xEiAb0t7s9+WZ6cyx8zdliiOl42ct1Szm/PpV2XH9FVXQVnfI0esvfpdGJhXto/FBwpq1foi2fR1U='
              '; WM_NIKE=9ca17ae2e6ffcda170e2e6ee99f333f48b8198d54086b88ba2d45f969e9eaab54295bffba6cc46b8b7e5a3b52af0fe'
              'a7c3b92a9c9abc96c55a8eb5bd93cf5baeadbd90f27bf794a8ccf67d888688d6fb7af29ea5a2ee738de9faace93b969381a6c63f'
              'f5eba58ab43dbc9ba7a2e13cb8e9bddaaa5d9aeaad9afb34babca48aec45b0ecfe84f73b91a6a3d0d37c96ee98a9bc4e96889fb7'
              'ed6e8bf0ab94f56eb4bc89abeb54b8b1e1a7c17db4afff87ee63f2ba9ed2d837e2a3; MUSIC_U=0593e4888f714b0c38be449dde'
              'd72f631a76b2fa248a2b853f1cd321ffc353859d5cb058ee9489a033a649814e309366; __csrf=6e362a5caa58eb5fc8297b7c1'
              'c3e0407; JSESSIONID-WYYY=QB\ZG13+gQhgfJ8+mn00X/mZD57jmYtYfSb1SdwWs2hSRJNu07sDv7jMtrX8lWkcMGNfxKO+eMx7p/X'
              'tIaWyB2nXkacx\DaxXQZPfdQ241s0UIKQZZnH+PSRy7ZdG+KNBH1\+6XIbUNqxZGCClwPxxOqwgPA2YSGrYkXnuPYFmmN8KH1:159931'
              '1290462',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '80.0.3987.122 Safari/537.36'
}

cookie_jar = RequestsCookieJar()
cookie_jar.set("cookie", headers['cookie'])
cookies = dict(cookies_are=headers['cookie'])

def get_playlist(url):
    data = requests.get(url, headers=headers)
    print(data.text)


if __name__ == '__main__':
    get_playlist('https://music.163.com/#/playlist?id=2568660671')
