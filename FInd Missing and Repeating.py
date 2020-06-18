# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 22:46:46 2020

@author: pussy
"""
t=int(input())
for q in range(t):
    n=int(input())
    l = input().split()
    for i in range(n):
        l[i] = int(l[i])
    su=n*(n+1)
    su=su//2
    s=sum(l)
    x=0
    for i in range(n):
        if l[abs(l[i])-1]>0:
            l[abs(l[i])-1] = -l[abs(l[i])-1]
        else:
            x=abs(l[i])
    f=abs(s-x)
    print(x,su-f)
    
    