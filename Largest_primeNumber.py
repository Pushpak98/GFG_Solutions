# -*- coding: utf-8 -*-
"""
Created on Wed May 27 10:25:14 2020

@author: pussy
"""


for _ in range(int(input())):
    a=int(input())
    i=1
    while(i<a):
        if a%i==0:
            b=[]
            b.append(i)
        i+=1
    print(max(b))
            