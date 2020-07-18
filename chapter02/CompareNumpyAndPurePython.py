#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-16 23:38:12
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import sys
from datetime import datetime
import numpy as np

def numpysum(n):
    a=np.arange(n)**2
    b=np.arange(n)**3
    c=a+b
    return c


def pythonsum(n):
    a=list(range(n))
    b=list(range(n))
    c=[]

    for i in range(len(a)):
        a[i]=i ** 2
        b[i]=i**3
        c.append(a[i]+b[i])

    return c

size=int(input("input your num"))

start=datetime.now()
c=pythonsum(size)
delta=datetime.now()-start
print("The last 2 elements of the sum", c[-2:])
print("PythonSum elapsed time in microseconds", delta.microseconds)


start1=datetime.now()
num=numpysum(size)
delta1=datetime.now()-start1
print("The last 2 elements of the sum", num[-2:])
print("NumPySum elapsed time in microseconds", delta1.microseconds)
