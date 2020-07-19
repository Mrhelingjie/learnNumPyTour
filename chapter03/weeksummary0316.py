#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-19 14:21:21
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np
from datetime import datetime

def datestr2num(s):
    # 读取时是字节字符串bytes 要对字符串进行解码 变成str
    return datetime.strptime(s.decode('ascii'),"%d-%m-%Y").date().weekday()


dates,open,high,low,close=np.loadtxt('data.csv',delimiter=',',usecols=(1,3,4,5,6),converters={1:datestr2num},unpack=True)

close=close[:16]
dates=dates[:16]

first_monday=np.ravel(np.where(dates==0))[0]
print('first_monday',first_monday)

last_friday=np.ravel(np.where(dates==4))[-1]
print('last_friday',last_friday)

weeks_indices=np.arange(first_monday,last_friday+1)
print("week init",weeks_indices)
# 分成三个周
weeks_indices=np.split(weeks_indices,3)
print("weeks indices after split",weeks_indices)

def summarize(a,o,h,l,c):
    monday_open=o[a[0]]
    week_high=np.max(np.take(h,a))
    week_low=np.min(np.take(l,a))
    friday_close=c[a[-1]]
    return("apple",monday_open,week_high,week_low,friday_close)

# apply_along_axis 对内的每个元素起作用
weeksummary=np.apply_along_axis(summarize,1,weeks_indices,open,high,low,close)
print(weeksummary)
np.savetxt("weeksummary.csv",weeksummary,delimiter=',',fmt="%s")