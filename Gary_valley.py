# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:06:37 2019

@author: pussy
"""

import math
import os
import random
import re
import sys
import re


#n=int(input())

st=list(map(str,input().split()))

#st=str(input())
#s = str[U,D]
#input_str = raw_input("Please provide some info: ")

#set(st) <= {"U", "D"}


for element in st:
    #if not re.match("(U\w+)\W(D\w+)",element):
    if  not re.match ['U','D']:
        print ("Error! Only letters U,D allowed!")
        sys.exit()
    elif len(st) > 8:
        print ("Error! Only 15 characters allowed!")
        sys.exit()
                
        
        