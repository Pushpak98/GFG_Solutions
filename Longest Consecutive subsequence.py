# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 22:49:20 2020

@author: pussy
"""

def findLongestConseqSubseq(arr, n):
    s=set(arr)
    ans=0
    for i in range(n):
        if arr[i]-1 not in s:
            j=arr[i]
            while(j in s):
                j+=1
            ans=max(ans,j-arr[i])
    return ans
            
if __name__ == '__main__':
    for _ in range(int(input())):
        n=int(input())
        arr=sorted(list(map(int,input().split())))
        print(findLongestConseqSubseq(arr, n))
        



'''
7
1 2 3 5 6 7 8

'''