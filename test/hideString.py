# -*- coding: utf-8 -*-


import T2I_core

#隐藏文字到图片和读取图片中的文字
sampleText = """
使用unicode(path,'utf-8')转换为unicode
不要再与其他str字符相加等操作不要再与其他str字符相加等操作不要再与其他str字符相加等操作
不要再与其他str字符相加等操作不要再与其他str字符相加等操作不要再与其他str字符相加等操作
python2文件路径有中文读取失败
使用unicode(path,'utf-8')转换为unicode
不要再与其他str字符相加等操作不要再与其他str字符相加等操作不要再与其他str字符相加等操作
不要再与其他str字符相加等操作不要再与其他str字符相加等操作不要再与其他str字符相加等操作
python2文件路径有中文读取失败
使用unicode(path,'utf-8')转换为unicode
不要再与其他str字符相加等操作不要再与其他str字符相加等操作不要再与其他str字符相加等操作
不要再与其他str字符相加等操作不要再与其他str字符相加等操作不要再与其他str字符相加等操作
python2文件路径有中文读取失败
使用unicode(path,'utf-8')转换为unicode
不要再与其他str字符相加等操作不要再与其他str字符相加等操作不要再与其他str字符相加等操作
不要再与其他str字符相加等操作不要再与其他str字符相加等操作不要再与其他str字符相加等操作
python2文件路径有中文读取失败
使用unicode(path,'utf-8')转换为unicode
不要再与其他str字符相加等操作不要再与其他str字符相加等操作不要再与其他str字符相加等操作
不要再与其他str字符相加等操作不要再与其他str字符相加等操作不要再与其他str字符相加等操作"""
samplePictureDir = r'E:\1.jpg'
outputPictureDir = r'E:\12.png'
#
# T2I_core.txt2Img(
#     photoDir=samplePictureDir,
#     message=sampleText,
#     outputFile=outputPictureDir
# )

pictureContainTextDir = r'E:\12.png'
message = T2I_core.img2Txt(
    photoDir=pictureContainTextDir
)
print(message)
