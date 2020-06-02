# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 18:28:48 2019

@author: pussy
"""


n = int(input().strip())
c = list(map(int,input().strip().split(' ')))
c.insert(n,0)


count = 0
i = 0
while (i < n-1):   
    i += (c[i+2] == 0)+1
    count += 1


print (c)    
print (count)

