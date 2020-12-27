# -*- coding: utf-8 -*-

"""
Author: XXM
date: 2020/8/15 10:21
desc: 
"""
import os
from ctypes import *
from functools import cmp_to_key

from PySide2.QtCore import QThread, Signal


def compare_string(first_str, second_str):
    """
    https://docs.microsoft.com/zh-cn/windows/win32/api/shlwapi/nf-shlwapi-strcmplogicalw
    Returns 1 if the string pointed to by psz1 has a greater value than that pointed to by psz2.
    Returns -1 if the string pointed to by psz1 has a lesser value than that pointed to by psz2.
    :param first_str:
    :param second_str:
    :return:0,1,-1
    """
    Shlwapi = windll.LoadLibrary("Shlwapi")
    return Shlwapi.StrCmpLogicalW(first_str, second_str)


class RenameThread(QThread):
    signal = Signal(object)

    def __init__(self, path, start_num, length=3):
        super().__init__()
        self.path = path
        self.start_num = 0 if start_num == '' else int(start_num)
        self.length = 3 if length == '' else int(length)

    def get_name_list(self, path):
        file_list = []
        for file in os.listdir(path):
            if file.lower().endswith('png') or file.lower().endswith('jpg'):
                file_list.append(file)
        file_list = sorted(file_list, key=cmp_to_key(compare_string))
        return file_list

    def rename_by_sort(self, file_list, path, indent):
        for i in range(len(file_list)):
            rename = str(i + 1 +self.start_num).zfill(indent) + '.' + file_list[i].split('.')[-1].lower()
            self.signal.emit(rename)
            os.rename(os.path.join(path, file_list[i]), os.path.join(path, rename))

    def run(self):
        file_list = self.get_name_list(self.path)
        self.rename_by_sort(file_list, self.path, self.length)
        name = self.path.split('\\')[-1]
        self.signal.emit(name + "重命名完成\n")
