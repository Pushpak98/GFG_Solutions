# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 02:54:22 2020

@author: pussy
"""
k=[]

for _ in range(int(input())):
    m=int(input())
    a=1 
    b=1
    for i in range(1,3*m):
       c=a+b
       a=b
       b=c
       if c%2==0:
          k.append(c)
    print(k[m-1]%1000000007)
            
      
           