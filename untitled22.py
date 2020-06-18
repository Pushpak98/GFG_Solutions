# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:32:31 2020

@author: pussy
"""

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    
    for i in range(len(a)):
        b[i]=a[i]
    for j in range(len(a)):
        if b[j]<=a[j]:
            print(j-i)    