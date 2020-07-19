#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-18 23:21:11
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np
# delimiter => 分隔符
# usecols => 使用列
# unpack =>是否集合到一个array
c,v=np.loadtxt('data.csv',delimiter=',',usecols=(6,7),unpack=True)
print(c)
print(v)