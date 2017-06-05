# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 18:08:14 2017

@author: stuparm
"""
import numpy as np



a = np.zeros((5,6))

print(a)

c = np.array([2,3])
a[c,2] = 4

print(a)