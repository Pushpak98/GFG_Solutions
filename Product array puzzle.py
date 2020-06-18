# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:54:23 2020

@author: pussy
"""
for _ in range(int(input())):
    m=int(input())
    a=list(map(int,input().split()))
    c=1
    for i in range(m):
        c*=a[i]  
    for i in range(m):
        print(int(c/a[i]),end=' ')
   
    
#10  3  5 6 2