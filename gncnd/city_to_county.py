# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 14:17:35 2016

@author: kitware
"""

state_init={}
with open("state_init.txt","r") as sF:
    for line in sF.readlines():
        terms=line.strip().split(",")
        state_init[terms[1]]=terms[0]
print state_init

unus=[]
csc=[]
c_s={}
result=open("city_state_county.txt","w")
with open("city_state_county_raw.txt","r") as cscF:
    for line in cscF.readlines():
        line=line.replace('\"',"")
        terms=line.split(",")
        if state_init.has_key(terms[4]):
            csc.append((terms[3],state_init[terms[4]],terms[5]))
            if c_s.has_key(terms[5]):
                print terms[5],c_s[terms[5]], line
            else:
                c_s[terms[5]]=state_init[terms[4]]
        else:
            unus.append(terms[4])
            #print terms[4]
print list(set(unus))
print len(csc)
for t in list(set(csc)):
    result.write(t[0]+","+t[1]+","+t[2])