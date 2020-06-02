# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 11:10:02 2019

@author: pussy
"""

# Python3 program to Find the two 
# repeating elements in a given array 

for _ in range(int(input())):
    x = input()
    x = x[::-1]
    j = 0
    for i in range(len(x)):
        j = j+(int(x[i])*(2**i))
               
print(j)
               