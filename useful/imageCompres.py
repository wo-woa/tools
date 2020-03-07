# -*- coding: utf-8 -*-

"""
Author: XXM
date: 2020/2/17 22:37
desc: https://www.cnblogs.com/li1992/p/10675769.html
    压缩图片到指定大小，主要是生成封面后进行压缩
"""

from PIL import Image
import os
import shutil


def get_size(file):
    # 获取文件大小:KB
    size = os.path.getsize(file)
    return size / 1024


def get_outfile(infile, outfile):
    if outfile:
        return outfile
    dir, suffix = os.path.splitext(infile)
    outfile = '{}-out{}'.format(dir, suffix)
    return outfile


def resize_image(infile, outfile='', x_s=1376):
    """修改图片尺寸
    :param infile: 图片源文件
    :param outfile: 重设尺寸文件保存地址
    :param x_s: 设置的宽度
    :return:
    """
    im = Image.open(infile)
    x, y = im.size
    y_s = int(y * x_s / x)
    out = im.resize((x_s, y_s), Image.ANTIALIAS)
    outfile = get_outfile(infile, outfile)
    out.save(outfile)


def compress_image(infile, outfile='', mb=150, step=10, quality=50):
    """不改变图片尺寸压缩到指定大小
    :param infile: 压缩源文件
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，KB
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """
    o_size = get_size(infile)
    outfile = get_outfile(infile, outfile)
    if o_size <= mb:
        shutil.copy(infile, outfile)
        return infile, o_size
    while o_size > mb:
        im = Image.open(infile)
        if quality - step < 0:
            break
        im.save(outfile, quality=quality)
        quality -= step
        o_size = get_size(outfile)
    return outfile, get_size(outfile)


def compress_folder():
    type = input("请输入图片压缩类型(1.文件夹（默认）。2.单文件)：")
    type = '1' if type == '' else type
    mb = input("请输入压缩目标(KB,默认150)：")
    mb = 150 if mb == '' else int(mb)
    step = input("请输入每次调整的压缩比率(默认10)：")
    step = 10 if step == '' else int(step)
    quality = input("请输入初始压缩比率(默认50)：")
    quality = 50 if quality == '' else int(quality)
    address = input("请输入压缩路径：")
    if type == '1':
        files = os.listdir(address)
        for each in files:
            print(each + '压缩中...')
            compress_image(os.path.join(address, each), mb=mb, step=step, quality=quality)
    else:
        compress_image(address, mb=mb, step=step, quality=quality)


if __name__ == '__main__':
    # i, a = compress_image(r'E:\[Lenxus][Hombretigre]\fmk10-out.jpg', mb=750, step=3, quality=4)
    # compress_image(r'E:/wf/漫画家/李子昂/封面/【沙豆狼汉化】朝鸡+鸡卵.jpg')
    compress_folder()
