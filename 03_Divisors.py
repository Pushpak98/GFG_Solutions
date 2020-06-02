# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 00:15:23 2020

@author: puss
"""

#count=0


for _ in range(int(input())):
    a=[]
    m=int(input())
    while(m>=4):
        b=[]
        for i in range(1,m+1):
            if m%i==0:
                b.append(i)
        #print(b)
        if len(b)==3:
           a.append(m)    
           #print(a)
        m-=1
    print(len(a))                        
                