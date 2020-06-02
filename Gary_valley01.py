# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 23:28:44 2019

@author: pussy
"""

n = input()
s = str(input())
 
level = 0
valleys = 0
for direction in s:
    if direction == "U":
        level += 1
        if level == 0:
            valleys += 1
    else:
        level -= 1
         
print (valleys)
