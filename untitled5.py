# -*- coding: utf-8 -*-
"""
Created on Sat May 23 18:39:15 2020

@author: pus
"""
'''
p = abs((int(x[1])-int(x[0])))
if (p == 1):
    print(,end=" ")
if arr[0]>arr[1]:
        k = range(1,arr[0])
    else:
        k =
'''
#import 

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    #arr = list((map(int,input().split())))
    #arr = arr.sort()
    #print(arr)
    k=[]
    for i in range(1,arr[0]):
        if (arr[0] % i == 0):
            if (arr[1] % i == 0):
                k.append(i)
               # print(i,end=" ")  
    print(max(k))
    