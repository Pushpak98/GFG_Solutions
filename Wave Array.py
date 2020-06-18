# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 23:56:35 2020

@author: pussy
"""


for i in range(int(input())):
    n=int(input())
    a=input().split()
    if n%2==0:
        for i in range(0,n,2):
            a[i]=a[i+1]
            a[i+1]=a[i]
        print(*a)
    else:
        for i in range(0,n-1,2):
            a[i],a[i+1]=a[i+1],a[i]
        print(*a)   