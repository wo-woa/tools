# -*- coding: utf-8 -*-

"""
Author: XXM
date: 2020/8/15 10:21
desc: 
"""
import os
from ctypes import *
from functools import cmp_to_key


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


def get_name_list(path):
    file_list = []
    for file in os.listdir(path):
        if file.lower().endswith('png') or file.lower().endswith('jpg'):
            file_list.append(file)
    file_list = sorted(file_list, key=cmp_to_key(compare_string))
    return file_list


def rename_by_sort(file_list, path, indent=3):
    for i in range(len(file_list)):
        rename = str(i+1).zfill(indent) + '.' + file_list[i].split('.')[-1]
        os.rename(os.path.join(path, file_list[i]), os.path.join(path, rename))


if __name__ == '__main__':
    main_path = 'E:\wf\漫画家\藤本郷\冲绳奴役岛\冲绳奴隶岛1-10 全集272P'
    main_file_list = get_name_list(main_path)
    rename_by_sort(main_file_list, main_path,indent=4)
