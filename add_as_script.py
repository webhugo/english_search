#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by webhugo on 17-5-14.

import os


temp = os.getcwd()
os.system("sudo rm /bin/pf")
# create a soft link
os.system("ln -s " + temp + "/index.py" + " /bin/pf")
