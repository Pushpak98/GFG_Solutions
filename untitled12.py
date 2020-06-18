"""
Created on Fri Jun 12 01:48:37 2020

@author: puss
"""

for _ in range(int(input())):
    x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    sum1=0
    sum2=0
    for i in range(x):
        for j in range(y):
            sum1+=a[j]
            sum2+=b[j]
            if sum1>=sum2:
                print(sum1)    
            else:
                print(sum2)
                
  
# 2 3 7 10 12
# 1 5 7 8


            
'''
            #print(sum1)
            #print(sum2)
            if sum1>=sum2:
                print(sum1)

        else a[i]==b[j]:
             sum1+=b[j]
             sum2+=a[j]
'''            
                
                         
                

