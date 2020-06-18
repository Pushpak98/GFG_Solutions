# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 02:46:32 2020

@author: pussy
"""

import math
for i in range(int(input())):
    n=int(input())
    a=(int(math.sqrt(2*n)))
    if a*(a+1)==2*i:
        print(1)
    else:
        print(0)
        
        