# -*- coding: utf-8 -*-

import json
import sys
import os

path=r'E:\tools\sqliteman-win32\Sqliteman-1.2.2\imageformats'
path='F:\手机\书\杂'
for root,dirs,files in os.walk(path):
    for i in files:
        print(i)
