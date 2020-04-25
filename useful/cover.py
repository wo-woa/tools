import os
import shutil
from ctypes import *
from functools import cmp_to_key
import imageCompres
from multiprocessing import Pool
import time, threading


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


remove_list = ['封面', '杂图']


class cover():
    def __init__(self, path):
        self.path = path
        self.save_path = path + '\\封面'
        self.folder_list = []

    def listdir(self):
        files = os.listdir(self.path)
        files.remove('封面')
        for each in files:
            fi = os.path.join(self.path, each)
            if os.path.isdir(fi):
                self.copy(each, os.path.join(self.path, each))

    def copy(self, name, path):
        '''
        :param name: 文件夹名字
        :param path: 文件夹路径
        :return:
        '''
        files = os.listdir(path)
        files = sorted(files, key=cmp_to_key(compare_string))
        for each in files:
            if not os.path.isdir(os.path.join(path, each)) and (
                    each.lower().find('jpg') > 0 or each.lower().find('png') > 0):
                # shutil.copy(os.path.join(path, each), os.path.join(self.save_path, name + each[-4:]))
                # print(name + '-----保存成功')
                # return os.path.join(self.save_path, name + each[-4:])
                return each
        print(name + "\033[31;49m没有符合的\033[0m")
        return ''

    def getImgFolderPaths(self, path):
        files = os.listdir(path)
        for each in remove_list:
            if each in files:
                files.remove(each)
        for each in files:
            fi = os.path.join(path, each)
            if os.path.isdir(fi):
                if not self.check_all_dir(fi):
                    m = {"name": each, "path": fi}
                    self.folder_list.append(m)
                    # print(fi)
                elif self.check_all_dir(fi):
                    self.getImgFolderPaths(fi)

    def getImagePath(self):
        for each in self.folder_list:
            files = os.listdir(each)
            files = sorted(files, key=cmp_to_key(compare_string))
            for each in files:
                if not os.path.isdir(os.path.join(path, each)) and (
                        each.lower().find('jpg') > 0 or each.lower().find('png') > 0):
                    pass

    def check_all_dir(self, path):
        files = os.listdir(path)
        if len(files) == 0:
            return False
        for i in files:
            if not os.path.isdir(os.path.join(path, i)):
                return False
        return True

    def mutiprocess_run(self):
        p = Pool(4)
        for file in self.folder_list:
            # self.copy_compress(i)
            # p.apply(self.copy_compress, args=(file,))
            # p.apply_async(self.copy_compress, args=(self,file,))
            p = threading.Thread(target=self.copy_compress, args=(file,))
            p.start()
        p.join()

    def copy_compress(self, file):
        save_file_name = self.copy(file["name"], file['path'])
        imageCompres.compress_image(os.path.join(file['path'], save_file_name),
                                    outfile=os.path.join(self.save_path, file["name"] + '.jpg'),
                                    quality=10, step=4)
        print(file["name"] + '-----压缩成功')


if __name__ == '__main__':
    path = r'E:\wf\漫画家\37.2℃'
    if not os.path.exists(path + '/封面'):
        os.chdir(path)  # 改变当前工作目录到指定的路径
        os.mkdir('封面')
    cover = cover(path)
    cover.getImgFolderPaths(path)
    cover.mutiprocess_run()
