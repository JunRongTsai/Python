# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:50:00 2018

@author: BlackRong
"""

N = int(input('输入需要对比大小数字的个数：\n'))

num=[ int(input('请输入第 %d 个对比数字 \n'%(i)))for i in range(1,N+1)]

print('您输入的数字为:',list(num))
print('最大值为: ',max(num))