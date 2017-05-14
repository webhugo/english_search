#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by webhugo on 17-5-14.


import os
import sys
import config
import codecs

global list
list = []
strl = "curl -s http://dict.cn/"
strr = """ | grep "<li><strong>" | tr -d '\t' | sed 's/<li><strong>//g' | sed 's/<\/li>//g' | sed 's/<\/strong>//g'
"""


def _get_index_file(char):
    for file in config.files:
        if char == file[file.rindex("/") + 1:file.rindex(config.postfix)]:
            return file


def _spider(word, file):
    str = strl + word + strr
    str = os.popen(str)
    str = str.read()
    sys.stdout.flush()


    str = str.split('\n')
    with open(file, 'a') as  file:
        flag = True  # 表示第一次写入
        for s in str:
            if not len(s) == 0:
                list.append(s)
                if flag == True:
                    file.write("\n")
                    file.write("|\t" + word + "\t|\t" + s + "\t|")
                    flag = False
                else:
                    file.write("\t" + s + "\t|")



def _search_local_file(word, file):
    with open(file) as file:
        for line in file:
            index = line.find("|")
            str = line[index:line.find("|",index+1)]
            if str.find(word) == -1:
                continue

            dict_list = line.split("|")
            for str in dict_list:
                str = str.strip()
                if not len(str) == 0:
                    list.append(str)

    if not len(list) == 0:
        return True
    else:
        return False


def search(word):
    del list[:]
    file = _get_index_file(word[0])
    if not _search_local_file(word, file):
        _spider(word, file)
    if len(list) == 0:
        print "no real word"
        return list
    list.pop(0)
    return list


