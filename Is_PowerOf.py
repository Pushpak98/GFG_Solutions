# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:52:55 2020

@author: pussy
"""

for _ in range(int(input())):
    a = list(map(int,input().split()))
    for i in range(0,10**5):
        if a[0]**i==a[1]:
            print(1)
            break
    else:
        print(0)