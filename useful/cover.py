import os
import shutil
from ctypes import *
from functools import cmp_to_key
import imageCompres


def compare_string(first_str, second_str):
    '''
    https://docs.microsoft.com/zh-cn/windows/win32/api/shlwapi/nf-shlwapi-strcmplogicalw
    Returns 1 if the string pointed to by psz1 has a greater value than that pointed to by psz2.
    Returns -1 if the string pointed to by psz1 has a lesser value than that pointed to by psz2.
    :param first_str:
    :param second_str:
    :return:0,1,-1
    '''
    Shlwapi = windll.LoadLibrary("Shlwapi")
    return Shlwapi.StrCmpLogicalW(first_str, second_str)


class cover():
    def __init__(self, path):
        self.path = path
        self.save_path = path + '\\封面'

    def listdir(self):
        files = os.listdir(self.path)
        files.remove('封面')
        for each in files:
            fi = os.path.join(self.path, each)
            if os.path.isdir(fi):
                self.copy(each, os.path.join(self.path, each))

    def copy(self, name, path):
        files = os.listdir(path)
        files = sorted(files, key=cmp_to_key(compare_string))
        for each in files:
            if not os.path.isdir(os.path.join(path, each)) and (each.lower().find('jpg') > 0 or each.lower().find('png') > 0):
                shutil.copy(os.path.join(path, each), os.path.join(self.save_path, name + each[-4:]))
                print(name + '-----保存成功')
                return

        print(name + "\033[31;49m没有符合的\033[0m")


path = input('请输入路径: ')
if not os.path.exists(path + '/封面'):
    os.chdir(path)  # 改变当前工作目录到指定的路径
    os.mkdir('封面')
cover = cover(path)
cover.listdir()
files = os.listdir(path + '/封面')
for each in files:
    print(each + '压缩中...')
    imageCompres.compress_image(os.path.join(path + '/封面', each), quality=20, step=4)
    os.remove(os.path.join(path + '/封面', each))
print('全部压缩完成')
input('运行完成，按任意键退出')
