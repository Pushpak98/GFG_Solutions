# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 01:37:13 2020

@author: pussy
"""

for _ in range(int(input())):
    a=[]
    n=int(input())
    a=list(map(int, input().split()))
    for i in range(0,n):
        for j in range(i,n):
            if a[i]<a[j]:    
                break
        else:
            print(a[i],end=' ')
          
            
          
'''
          b.append(a[i])   
        
    print( " ".join( str(e) for e in b ) )
    
'''