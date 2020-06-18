# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 00:08:40 2020

@author: pussy
"""

t=int(input())
for i in range(t):
    n=int(input())
    count=0
    x=1
    y=1
    z=0
    while(count!=n):
        z=x+y
        x=y
        y=z
        if(z%2==0):
            count=count+1
            result=z%1000000007
    print(result)