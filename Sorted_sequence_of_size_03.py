# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 22:22:23 2020

@author: pussy
"""

for _ in range(int(input())):
    m=int(input())
    arr=list(map(int,input().split()))
    b=[]
    arr.sort()
    for i in range(m):
        for j in range(i,m):
            if arr[i]<arr[j]:     
                b.append(arr[i])
    print(b)
                
                
        