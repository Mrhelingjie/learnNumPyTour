#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-18 18:27:08
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

b=np.arange(24).reshape(2,12)
print(b)
# 维度
print(b.ndim)
# 数组元素个数
print(b.size)
# 数组元素在内存中字节数
print(b.itemsize)
# 数组所占储存空间
print(b.nbytes)
# 数组所占储存空间
print(b.size*b.itemsize)

# resize修改时自身修改
b.resize(6,4)
print(b)
# T属性与transpose函数一样
print(b.T)
b.resize(24,1)
# 一维数组T属性为原数组
print(b.T)


# 复数数组
com=np.array([1+1.j,3+2.j])
print(com)

# 输出复数实部
print(com.real)
# 输出复数虚部
print(com.imag)
# 元素类型
print(com.dtype)
print(com.dtype.str)

# flat属性是获得flatiter对象的唯一方式
b.resize(6,4)
f=b.flat
# 内存地址
print(f)
# 迭代输出
for it in f:
    print(it)
# 按下标输出数组元素    
print(f[2])
print(f[[1,5,10]])
# 用flat对全部元素进行修改
b.flat=100
print(b)
# 用flat对指定索引元素进行修改
b.flat[[1,4,6]]=1
print(b)