# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 11:28:28 2019

@author: pussy
"""

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

genre_counting={}

for i in apps_data[1:]:
    genre=i[11]
    
    if genre in genre_counting:
        genre_counting[genre]+=1
    else:
        genre_counting[genre]=1

print(genre_counting)  