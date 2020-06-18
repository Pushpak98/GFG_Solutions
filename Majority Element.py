# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 00:55:18 2020
@author: puss
"""

for _ in range(int(input())):
    m=int(input())
    a=list(map(int,input().split()))
    for i in range(len(a)):
        a.count(a[i])
        if a.count(a[i])>int(len(a)/2):
            print(a[i])
            break
    else:
        print(-1)
   
    
'''    
    for i in range(len(a)):
        if a.count(a[i])>int(len(a)/2):
            print(a[i])      
        else:
            print(-1)
    
        
        
       for j in range(i+1,len(a)):
            if a[i]==a[j]:
                count+=1
    print(count)

            if count>len(a)/2:
                print(a[i])
            else:
                 print(-1)
'''                         
                       