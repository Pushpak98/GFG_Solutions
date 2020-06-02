# -*- coding: utf-8 -*-
"""
Created on Sat May 30 01:57:04 2020

@author: pussy
"""

for _ in range(int(input())):
    k=[]
    m=int(input())
    s=m
    while(m>2):
        for i in range(2,m):        
            if m%i==0:
                break
        else:
            k.append(m)
        m-=1
    k.append(2) 
    k.sort()
    #print(len(k))
    #print(s)
        
    for j in range(len(k)):
        for n in range(len(k)):
            if ((k[j])*(k[n])<=s):   
                print((k[j],k[n]),end=" ")
            else:
                print()
                