# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 00:40:31 2020

@author: pus
"""
#import math


p=1
count=0
for _ in range(int(input())):
    m=int(input())
    for i in range(1,m):
        p*=(m-i)
    k=p*m 
    print(k)
    k=str(k)
    count=len(k)-len(k.rstrip('0'))
    print(count)
    
'''
    if (p*m)/10==0:
        count+=1
        print(count)
    else:
        print(count)
'''
    
        
        