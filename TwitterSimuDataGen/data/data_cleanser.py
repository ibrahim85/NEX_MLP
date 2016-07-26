# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 12:38:16 2016

@author: kitware
"""

words=[]
with open("words.txt","r") as of:
    for line in of.readlines():
        line='[^\w]', ' 'line
        if len(line.split())>1:
                words.extend(line.strip('\'"?,.-').split())
        words.append(line.strip())
for word in words:
    print word