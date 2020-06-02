# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 13:03:59 2019

@author: pussy
"""

n=int(input())
arr=list(map(int,input().split()))
arr2=list(set(arr))
arr3=[]
for i in arr2:
    if arr.count(i)>1:
        arr3.append(arr.count(i)//2)
print(arr2)
print(arr3)


def du(arr4):
    m=0
    for i in arr4:
        m+=i
    return m

print(du(arr3))



