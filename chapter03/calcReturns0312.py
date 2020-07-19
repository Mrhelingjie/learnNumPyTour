#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-19 13:25:53
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

c=np.loadtxt('data.csv',delimiter=',',usecols=(6,),unpack=True)
# diff比输入数组少一个元素
l=np.diff(c)
# 输出原数组与diff之后的数组
print(c)
print(l)
print(c[:-1])
l_return=np.diff(c)/c[:-1]
# std函数计算标准差
print('标准差',np.std(l_return))
# 对数收益率
log_return=np.diff(np.log(c))

afterProcessLog=np.where(l_return>0)
print('>0的索引',afterProcessLog)

annual_vol=np.std(log_return)/np.mean(log_return)
annual_vol=annual_vol/np.sqrt(1./252.)

print('年波动率',annual_vol)
print('月波动率',annual_vol*np.sqrt(1./12.))