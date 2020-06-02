# -*- coding: utf-8 -*-
"""
Created on Wed May 27 00:20:58 2020

@author: pussy
"""

#code
t=1  
for i in range(int(input())):
    a=int(input())
    if a==0: 
        print(1)
    if a==1:
        print(1)
    else:   
        for j in range(2,a+1):  
            t*=j  
        print(t)
        