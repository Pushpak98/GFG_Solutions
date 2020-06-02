# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:53:00 2020

@author: puss
"""

for _ in range(int(input())):
    a=list(map(int,input().split()))
    #print(a[0])
    if (a[0]==a[1]==a[2]==a[3]==a[4]==a[5]==a[6]==a[7]):
        print('No')
    elif(abs(a[0]-a[6])==abs(a[2]-a[4]) and abs(a[1]-a[5])==abs(a[3]-a[7])):
        print('Yes')
    else:
        print('No')
        
    