# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 01:53:42 2020

@author: pus
"""

for _ in range(int(input())):
    m=int(input())
    sum=0          
    for i in range(1,m+1):
        sum+=i
        if sum==m:
            print(1)
            break
    else:
        print(0)
    
        
    