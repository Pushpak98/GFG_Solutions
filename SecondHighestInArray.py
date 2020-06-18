# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 02:39:36 2020

@author: pussy
"""

for _ in range(int(input())):
    m=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    #print(arr[len(arr)-2])
    
    
    arr.reverse()
    print(arr)