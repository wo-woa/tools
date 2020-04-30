# -*- coding: utf-8 -*-

'''
Author: XXM
date: 2020/4/30 23:27
desc: kit
'''
import shutil, os


def pixeval_img_convert(path):
    ''' make a/0.jpg to a#0.jpg
    :param path: pixeval download path
    :return:
    '''
    for root, dirs, files in os.walk(path, topdown=False):

        for name in dirs:
            dir_path = os.path.join(root, name)
            files = os.listdir(dir_path)
            os.chdir(dir_path)
            for i in files:
                new_name = name + "#" + i
                os.rename(i, new_name)
                shutil.move(os.path.join(dir_path, new_name), os.path.join(path, new_name))


if __name__ == '__main__':
    pass
