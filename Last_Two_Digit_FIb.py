# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 00:44:00 2020
@author: pussy
"""

k=[]
for _ in range(int(input())):
    m=int(input())
    a=0 
    b=1
    count=1
    while(count!=(m+1)):
       c=a+b
       a=b
       b=c
       k.append(c)
       count+=1
    if m==0:
        print('00')
    if m==1:
        print('01')
    else:
        #print(k[m-2])
        print("{:02d}".format(k[m-2]))
               
               