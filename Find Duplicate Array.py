# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 00:14:50 2020

@author: pussy


"""

from collections import Counter

def duplicates(arr, n):
    dups = Counter(arr) - Counter(set(arr))
    if len(dups)==0:
        return [-1]
    else:        
        return sorted(list(dups.keys()))

    