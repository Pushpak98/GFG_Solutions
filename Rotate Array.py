# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 22:14:36 2020

@author: pussy
"""
b=[]
for _ in range(int(input())):
    x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=a[y:x]
    c=a[:y]
    c= " ".join(str(e) for e in c)
    b.append(c)
    print( " ".join( str(e) for e in b ) )
    
    