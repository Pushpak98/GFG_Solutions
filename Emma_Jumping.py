# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:10:11 2019

@author: pushpak
"""

n=int(input())
#s=(map(int,input()))
s = list(map(int, input().strip().split()))
s.insert(n,0)
#print(p)
push=0

#print(s)
#print(p)


step=0
count=0

while (step<n-1):
    if s[step+2]==0:
        count+=1
        step=step+2
        
    elif s[step+2]==1:        
        count+=1
        step=step+1
    #step+=(s[step+2==0])+2
        
    
print(count)



'''    
   if s[step] == 0:
        if s[step+2]==0:
            push+=1
            step=step+2
        elif s[step+2]==1:
            push+=1
            step=step+1
            
print(push)
        
  '''  
  
  