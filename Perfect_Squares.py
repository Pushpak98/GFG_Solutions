# -*- coding: utf-8 -*-
"""
Created on Sun May 31 00:32:40 2020

@author: pussy
"""

count=0
for _ in range(int(input())):
    m=int(input())
    for i in range(1,m):
        for j in range(1,i+1):
            if i%j==0:
                if i==j*j:
                    count+=1

print(count)
                
            
            
            