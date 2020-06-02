# -*- coding: utf-8 -*-
"""
Created on Sat May 30 01:13:49 2020

@author: pussy
"""


for _ in range(int(input())):
    m=int(input())
    if m==2:
        print(m)
    else:
        n=2
        while(m>2):
            while(n<=m):
                for i in range(2,n):        
                    if n%i==0:
                        break
                else:
                    print(n,end=" ")    
                n+=1   
            m-=1
        print()
        


