# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 01:24:02 2020

@author: pussy
"""

for _ in range(int(input())):  
    x,y=map(int,input().split())
    b=x*y
    for i in range(2,min(x,y)+1):
        b+=(x-i+1)*(y-i+1)
    print(b)
    
    
    # -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 01:24:02 2020

@author: pussy

for _ in range(int(input())):
n,m = map(int,input().split())
ans = n*m
for i in range(2,min(n,m)+1):
    ans += (n-i+1)*(m-i+1)
print(ans)

"""