# -*- coding: utf-8 -*-

"""
Author: XXM
date: 2020/8/15 10:21
desc: 
"""
import os
from ctypes import *
from functools import cmp_to_key
import re


def compare_string(first_str, second_str):
    """
    按照windows的文件名排序规则，如11.jpg会大于2.jpg
    https://docs.microsoft.com/zh-cn/windows/win32/api/shlwapi/nf-shlwapi-strcmplogicalw
    Returns 1 if the string pointed to by psz1 has a greater value than that pointed to by psz2.
    Returns -1 if the string pointed to by psz1 has a lesser value than that pointed to by psz2.
    :param first_str:
    :param second_str:
    :return:0,1,-1
    """
    Shlwapi = windll.LoadLibrary("Shlwapi")
    return Shlwapi.StrCmpLogicalW(first_str, second_str)


def my_input(tip, pattern=None, default=None):
    while True:
        text = input(tip)
        data = None
        if text == '' and default != None:
            return default
        if pattern:
            data = re.match(pattern, text)
        if data:
            return text
        else:
            print("请输入正确格式！")


def compare_by_ascii(first_str, second_str):
    for i in range(len(first_str)):
        if first_str[i] > second_str[i]:
            return 1
        elif first_str[i] < second_str[i]:
            return -1
    if len(first_str) > len(second_str):
        return -1
    else:
        return 1


def reverse_compare_by_ascii(first_str, second_str):
    return -1 if compare_by_ascii(first_str, second_str) == 1 else 1


def get_name_list(path, compare):
    file_list = []
    for file in os.listdir(path):
        if file.lower().endswith('png') or file.lower().endswith('jpg'):
            file_list.append(file)
    file_list = sorted(file_list, key=cmp_to_key(compare))
    return file_list


def rename_by_sort(file_list, path, indent=3, start=0):
    for i in range(len(file_list)):
        rename = str(i + 1 + start).zfill(indent) + '.' + file_list[i].split('.')[-1]
        os.rename(os.path.join(path, file_list[i]), os.path.join(path, rename))


if __name__ == '__main__':
    while True:
        main_path = my_input('请输入路径: ', r'^\w:\\.+$')
        start = int(my_input('请输入起始(默认0): ', '^\d+$', '0'))
        indent = int(my_input('请输入长度(默认3): ', '^\d$', '3'))
        compare_type = my_input('请输入排序方式:1. windows自带排序(默认) 2.ascii排序', '^\d$', '1')
        compare_type = compare_string if compare_type == '1' else compare_by_ascii
        main_file_list = get_name_list(main_path, compare_type)
        rename_by_sort(main_file_list, main_path, indent, start)
        if input('重命名完成！回车退出，非空继续:') == '':
            break

    # print(compare_string('11a','2a'))
    # print(compare_by_ascii('11a', '2a'))
