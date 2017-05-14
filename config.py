#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by webhugo on 17-5-14.

import os


def _files():
    # 创建目录dict
    if not os.path.exists(dict_dir):
        os.mkdir(dict_dir)

    chs = [x + ord('a') for x in range(0, 26)]
    files = map(lambda x: os.path.join(dict_dir, chr(x) + '.txt'), chs)
        # 创建文件和修改可写
    for file in files:
        if not os.path.exists(file):
            os.mknod(file)
            os.chmod(file, 0o777)  # python需要八进制


    return files


# export
dict_dir = os.path.join("./", "dict")
files = _files()
postfix = ".txt"

url = "http://dict.cn/"
installPath = "/opt/pf/"
