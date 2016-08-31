# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 13:52:27 2016

@author: kitware
"""
countyF=open("USA_ghcnd-stations-loc_countyLevel.txt","w")
count=0
scount=0
with open("USA_ghcnd-stations-loc_city_states.txt","r") as cF:
    for line in cF.readlines():
        scount+=1
        terms=line.split()
        if terms[3].endswith("County"):
            countyF.write(terms[0]+" "+terms[1]+" "+ terms[2]+" "+terms[3].split("_")[0]+"\n")
        elif terms[4].endswith("County"):
            countyF.write(terms[0]+" "+terms[1]+" "+ terms[2]+" "+terms[4].split("_")[0]+"\n")
        else:
            print terms[3],terms[4]
            count+=1

print str(scount)+"/"+str(count)



