# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 00:51:33 2020

@author: pus
"""

count=0

for _ in range(int(input())):
    a=int(input())
    for i in range(1,a+1):
        for j in range(1,a+1):
            if j%i==0:
                count+=1 
    print(count)
            