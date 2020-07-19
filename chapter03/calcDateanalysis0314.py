#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-19 13:51:38
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np
from datetime import datetime

def datestr2num(s):
    # 读取时是字节字符串bytes 要对字符串进行解码 变成str
    return datetime.strptime(s.decode('ascii'),"%d-%m-%Y").date().weekday()


dates,close=np.loadtxt('data.csv',delimiter=',',usecols=(1,6),converters={1:datestr2num},unpack=True)

print(dates)
# 周一到周五的均价
averages=np.zeros(5)

for i in range(5):
    indices=np.where(dates==i)
    # 按照indices中下标取值
    prices=np.take(close,indices)
    avg=np.mean(prices)
    print('Day',i,"prices",prices,"avg",avg)
    averages[i]=avg


top_avg=np.max(averages)
print(top_avg)
top_day=np.argmax(averages)
print(top_day)

bottom_avg=np.min(averages)
bottom_day=np.argmin(averages)
print(bottom_avg)
print(bottom_day)