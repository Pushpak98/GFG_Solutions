#code# -*- coding: utf-8 -*-
"""
Created on Thu May 21 23:55:14 2020

@author: pussy
"""

for _ in range(int(input())):
    x = input()
    #x = int(input())
    for i in range((int(x)+1)):
        if (int(x)<=10):
            print(i,end=" ")
        #for j in range(len(x)):
        elif(abs((int(x[1])-int(x[0]))) == 1):
            #for j in range(x):
            print(i,end=" ")
        else:
            print()