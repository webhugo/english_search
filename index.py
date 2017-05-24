#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by webhugo on 17-5-14.

'''
1. 每次搜索文件，先从本地文件中查找
2. 这里做一个优化，分为26个文件夹，分别是a，b...,z开头的，这样可以减少搜索时间
3. 如果找不到，则通过爬虫获取
'''

import os
from search import search
import sys

str = """
################cl- 清屏
################ex- 退出
"""

print str


def start():
    word = command = raw_input(">>>> ")
    if command == "cl-":
        os.system("clear")
        return
    elif command == "ex-":
        exit(0)
        return

    dict_list = search(word)
    if not len(dict_list) == 0:
        for dict in dict_list:
            try:
                str = "\t" + dict
                print str
            except:
                pass
        # print dict_list
    print "###########################"


while True:
    start()
