# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:47:35 2020

@author: puss


for i in range(int(input()):
    num = int(input())  
        if num > 1:  
           for i in range(2,num):  
               if (num % i) == 0:  
                   print('No')
                   break  
           else:  
               print('Yes')  
               
        else:  
           print('No')  
           
           
"""   


for _ in range(int(input())):
    m=int(input())
    if m>1:
        for i in range(2,m):
            if m%i==0: 
                print('No')
                break
        else:
            print('Yes')
    else:
        print('Yes')

        
        
        