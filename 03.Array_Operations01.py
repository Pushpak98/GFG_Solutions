# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 23:59:17 2020

@author: pussy
"""


def searchEle(a, x):
    a.index(x)
    return True
def insertEle(a, y, yi):    
    a.insert(y,yi)
    return True
def deleteEle(a, z):
    a.remove(z)
    return True


        
print(searchEle([1,2,3,4],2))
print(insertEle([1,2,3,4],2,2))
print(deleteEle([1,2,3,4],2))

