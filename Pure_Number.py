# -*- coding: utf-8 -*-
"""
Created on Wed May 27 23:03:26 2020

@author: pussy
"""

for _ in range(int(input())):
    m=int(input())
    count=0
    for i in range(m+1):
        for j in range(m):
            if (i*i*i==m) or (j*j*j==m):
                count=1
            elif (i*i*i+j*j*j==m):
               count+=1
    print(count)
    92
    