# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 00:50:21 2020

@author: pussy
"""

from collections import Counter
for _ in range(int(input())):
    m=int(input())
    arr=list(map(int,input().split()))
    b=arr
    for x in set(arr):
        arr.remove(x)
    arr = sorted(list(set(arr)))
    print(b)

'''    
    #d=counter([1:m])-counter(set(arr))
    #print(min(arr))
    #print(list(d.key()))
    for i in range(len(arr)):
       if (i+1)!=arr[i]:
           print(arr[0])
   
    print(min(arr),i)
            
    
'''
    