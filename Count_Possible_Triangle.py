# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 00:39:08 2020

@author: pussy
"""



import math
for _ in range(int(input())):
    n=int(input())
    m=list(map(int, input().split()))
    for x in m:
        if m.count(x)>1:
           m.remove(x)
    print(len(m))
    print(int(math.factorial(len(m))/(math.factorial(len(m)-3)*math.factorial(3))))
    