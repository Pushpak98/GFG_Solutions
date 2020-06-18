# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 22:42:07 2020

@author: pus
"""
for _ in range(int(input())):
    n=int(input())
    a=[int(_) for _ in input().split()]
    #a=list(map(int,input().split()))
    k=int(input())
    flag=0
    i=0
    j=n-1
    
    while(i<j):
        if a[i]+a[j]==k:
            flag=1
            print(a[i],a[j],k)
            i+=1
            j-=1
        elif a[i]+a[j]<k:
            i+=1
        else:
            j-=1
    if flag==0:
        print(-1)
        


    if flag==0:
        print(-1)