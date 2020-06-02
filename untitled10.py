# -*- coding: utf-8 -*-
"""
Created on Tue May 26 23:40:44 2020

@author: pussy
"""

import math 
  
# prints 12 
#print (math.gcd(60,48)) 
    
    
t=int(input())
for i in range(t):
    size=int(input())
    li=list(map(int,input().split()))
    x=li[0]
    for i in range(1,size):
        #print(math.gcd(x,li[i]))
        x= math.gcd(x,li[i])
    print(x)
    
    
    #print(x)