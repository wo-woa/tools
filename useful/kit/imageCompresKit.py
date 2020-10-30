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
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from PySide2.QtCore import QThread, Signal


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


def get_size(file):
    # 获取文件大小:KB
    size = os.path.getsize(file)
    return size / 1024


def get_outfile(infile, outfile):
    """ 如果格式为png，压缩效率会比较低,默认jpg
    :param infile:
    :param outfile:
    :return:
    """
    if outfile:
        return outfile
    dir, suffix = os.path.splitext(infile)
    outfile = '{}-out{}'.format(dir, '.jpg')
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


class CompressThread(QThread):
    signal = Signal(object)

    def __init__(self, address, type, mb, step, quality):
        super().__init__()
        self.address = address
        self.type = type
        self.mb = mb
        self.step = step
        self.quality = quality

    def compress_image(self, infile, outfile='', mb=150, step=10, quality=50, name=None):
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
            im = im.convert('RGB')
            im.save(outfile, quality=quality)
            quality -= step
            o_size = get_size(outfile)
        if name:
            self.signal.emit(name + "压缩完成")
        return outfile, get_size(outfile)

    def run(self):
        files = os.listdir(self.address)
        with ThreadPoolExecutor(max_workers=5) as t:
            obj_list = []
            for each in files:
                obj = t.submit(self.compress_image, os.path.join(self.address, each), mb=self.mb, step=self.step,
                               quality=self.quality,
                               name=each)
            for future in as_completed(obj_list):
                future.result()
        name = self.address.split('\\')[-1]
        self.signal.emit(name + "压缩完成\n")
