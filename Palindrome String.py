# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 23:05:13 2020

@author: pussy
"""

for _ in range(int(input())):
    m=int(input())
    a=str(input())
    b=[char for char in a]
    
    flag=0
    for i in range(m):
        if b[i]==b[(m-1)-i]:
            flag=1
        else:
            break
        
    if flag==1:
        print('Yes')
    else:
        print('No')
            
        

    
    
    
    
    
        