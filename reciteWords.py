# -*- coding: utf-8 -*-
import random


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


def recite(words):
    wrong = 0
    wrong_words = []
    print('total is ' + str(len(words)))
    for each in words:
        print(each[0], end='')
        input()
        pprint(each[1:])
        i = input()
        if i != '':
            wrong += 1
            wrong_words.append(each)
    print('answer wrong ' + str(len(wrong_words)))
    for i in wrong_words:
        pprint(i)


a = read_words('word')
recite(a)
