#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
#print("enter the n")
#print("enter the array")
#n = int(input())
#ar = list(map(int, input().rstrip().split()))
push=[]
        
def sockMerchant(n, ar):      
    for i in range(n):
        for j in range(i+1,n):
            if ar[j] == ar[i]:
                push.append(format(i))
                break
            break
        
    
               # ar.pop()
                
    arr_size = len(push)
    print(arr_size)
    return arr_size
        
n=5
ar= [1, 1, 1, 1, 1]


sockMerchant(n,ar)
