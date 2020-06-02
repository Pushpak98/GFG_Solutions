# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 01:31:43 2020

@author: pussy
"""

import math

p=1
count=0
for _ in range(int(input())):
    m=int(input())
    k=math.factorial(m)
    k=str(k)
    count=len(k)-len(k.rstrip('0'))
    print(count)
   
    
        
        
    