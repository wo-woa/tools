# -*- coding: utf-8 -*-
import random
import xlrd
import traceback


class word():
    def __init__(self, japanese, pronounce, type, meaning, sentence):
        self.japanese = japanese
        self.pronounce = pronounce
        self.type = type
        self.meaning = meaning
        self.sentence = sentence

    def answer(self):
        return self.pronounce + '\t' + self.type + '\t' + self.meaning + '\t' + self.sentence

    def total(self):
        return self.japanese + '\t' + self.answer()


def get_xls_day_words(name, sheet_num, start):
    workbook = xlrd.open_workbook(name)
    word_list = []
    sheet = workbook.sheet_by_index(sheet_num + 1)
    num = 1
    try:
        for i in range(sheet.nrows):
            row = sheet.row_values(i)
            if str(row[1]) == '' and str(row[0]) != '':
                if num == start:
                    i += 1
                    row = sheet.row_values(i)
                    while (row[1] != ''):
                        w = word(row[1], row[2], row[3], row[4], row[5])
                        word_list.append(w)
                        i += 1
                        row = sheet.row_values(i) if i < sheet.nrows else ['', '']
                    break
                else:
                    num += 1
    except Exception as e:
        print(traceback.format_exc())
    random.shuffle(word_list)
    return word_list


def get_xls_week_words(name, sheet_num):
    workbook = xlrd.open_workbook(name)
    word_list = []
    sheet = workbook.sheet_by_index(sheet_num + 1)
    try:
        for i in range(sheet.nrows):
            row = sheet.row_values(i)
            if str(row[1]) != '':
                w = word(row[1], row[2], row[3], row[4], row[5])
                word_list.append(w)
    except Exception as e:
        print(traceback.format_exc())
    return word_list


def pprint(list):
    for i in list:
        print(i, end='	')
    print()


def read_words(url):
    word_list = []
    with open(url, encoding='utf-8') as txt:
        data = txt.readlines()
    for each in data:
        if each != '\n':
            line = each[:-1].split('	')
            word_list.append(line)
    random.shuffle(word_list)
    return word_list


def recite(words, num=20):
    wrong = 0
    wrong_words = []
    print('total is ' + str(len(words)))
    for each in words:
        if wrong < num:
            print(each[0], end='')
            input()
            pprint(each[1:])
            i = input()
            if i != '':
                wrong += 1
                wrong_words.append(each)
        else:
            break
    print('answer wrong ' + str(len(wrong_words)))
    for i in wrong_words:
        pprint(i)


def recite_words(words, num=20):
    wrong = 0
    wrong_words = []
    print('total is ' + str(len(words)))
    for each in words:
        if wrong <= num:
            print(each.japanese, end='')
            input()
            print(each.answer())
            i = input()
            if i != '':
                wrong += 1
                wrong_words.append(each)
    print('answer wrong ' + str(len(wrong_words)))
    for i in wrong_words:
        print(i.total())


def review_day():
    week = input('请输入第几周  ')
    day = input('请输入第几天  ')
    week = 4 if week == '' else week
    day = 5 if day == '' else day
    words = get_xls_day_words(r'f:\nihong.xls', int(week), int(day))
    return words


def review_week():
    week = input('请输入第几周  ')
    week = 4 if week == '' else week
    words = get_xls_week_words(r'f:\nihong.xls', int(week))
    return words


def review_typical():
    a = read_words('word')
    return a


def get_type(num):
    return {
        "1": review_day,
        "2": review_week,
        "3": review_typical
    }.get(num, None)


while True:
    type = input('请输入复习类型：1(默认)：按天；2：按周；3：特定')
    type = '1' if type == '' else type
    words = get_type(type)()
    if type != '3':
        recite_words(words, 30)
    else:
        recite(words)
    if input('空格键继续，其他键退出') != ' ':
        break
