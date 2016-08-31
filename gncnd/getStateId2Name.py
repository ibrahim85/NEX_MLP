# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 15:27:05 2016

@author: kitware
"""

import json
with open("state_GEEJson.json") as gj:
    state=json.load(gj)
print state.keys(),len(state["features"]),dict(state["features"][0])["properties"]
sta_id={}
for i in range(len(state["features"])):
    #print i
    item=dict(dict(state["features"][i])["properties"])
    sta_id[item["STATE"]]=item["NAME"]
    print item["NAME"],item["STATE"]


cf=open("county_state.txt","w")

with open("gz_2010_us_050_00_500k.json") as cgj:
    county=json.load(cgj)
print county.keys(),len(county["features"]),dict(county["features"][0])["properties"]

counties=[]
for i in range(len(county["features"])):
    #print i
    item=dict(dict(county["features"][i])["properties"])
    counties.append((item["NAME"],item["COUNTY"],sta_id[item["STATE"]]))
    print item["NAME"],item["COUNTY"]
print len(counties),len(list(set(counties)))
for terms in list(set(counties)):
    cf.write(terms[0]+" "+terms[1]+" "+terms[2]+"\n")

