# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 11:47:14 2016

@author: kitware
"""
sta_ll={}
with open("USA_ghcnd-stations-loc_all.txt","r") as llF:
    for line in llF.readlines():
        line=line.strip()
        terms=line.split()
        sta_ll[terms[0]]=terms[1]+","+terms[2]

sta_info=[]
sta_dic={}
with open("NewUSA_ghcnd-stations-loc_all.txt","r") as nF:
    for i,line in enumerate(nF.readlines()):
        line=line.replace("\n","")
        terms=line.split(",")
        sta_info.append((terms[0],sta_ll[terms[0]],terms[1],terms[2]))
        sta_dic[terms[0]]=i


sta_cityF=open("station_USA_CityLevel_Location.csv","w")
total_count=0
count=0
with open("station_Loc.csv") as aF:
    for line in aF.readlines():
        #print line.split(",")
        terms=line.replace("\"","").split(",")
        #for term in terms:
        total_count+=1
        if len(terms[6])<1:
            if sta_dic.has_key(terms[0]):
                sta_info_e=sta_info[sta_dic[terms[0]]]
                ### station_id,latitude,longitude,city,state
                sta_cityF.write(terms[0]+","+sta_info_e[1]+","+sta_info_e[2]+","+sta_info_e[3]+"\n")
                count+=1
            else:
                continue
        else:
            sta_cityF.write(terms[0]+","+terms[1]+","+terms[2]+","+terms[6]+","+terms[7]+"\n")
            count+=1
            #print terms[8]


print total_count-count,count,"/",total_count
