# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 00:40:51 2020

@author: pussy
"""

for _ in range(int(input())):
    a=list(map(str,input().split()))
    #a=str(input())
    #b=[char for char in a]
    #print(a)
    
    #for i in range(len(a)):
    if sorted([char for char in a[0]]) == sorted([char for char in a[1]]):
        print('Yes')
    else:
        print('No')
    