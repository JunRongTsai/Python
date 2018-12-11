# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:17:34 2018

@author: BlackRong
"""

number = input('輸入一串數字:')

numlist=[int( number[item: item+1] ) for item in range(0, len(number), 1)]
print (numlist)
print (max(numlist))