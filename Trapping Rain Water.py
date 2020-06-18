# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 01:53:27 2020

@author: pussy
"""

for _ in range (int(input())):
    n = int(input())
    arr = list(map(int,input().split( )))
    mxl = [0]*n
    mxr = [0]*n
    mxl[0] = arr[0]
    for i in range(1,n):
        mxl[i] = max(mxl[i-1],arr[i])
        mxr[n-1] = arr[n-1]
    for i in range (n-2,-1,-1):
        mxr[i] = max(mxr[i+1],arr[i])
        water = [0]*n
    for i in range (n):
        water[i] = min(mxl[i], mxr[i]) - arr[i]
    Z = sum(water)
    print(Z)