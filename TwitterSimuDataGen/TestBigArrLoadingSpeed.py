# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 09:31:40 2016

@author: kitware
"""
import json,time


#data.append([i for i in range(1000000)])
#data.append([j for j in range(100000000)])
t1=time.time()
with open("TwitterGen/twitterSimuData96Fea3Class500.json","r") as jf:
  data=json.load(jf)
print "Loading time:",time.time()-t1



print len(data[0]),len(data[2])