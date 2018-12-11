# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 16:03:53 2018

@author: BlackRong
"""

import random
 
a = [random.randint(0,99) for _ in range(7)]
print (a)

x=0
y=0
for i in range(0,len(a)):
    if (a[i]%2)==0:
        x=x+1
    else:
        y=y+1
        
print(y,'個奇數')
print(x,'個偶數')
