# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:23:59 2016

@author: kitware
"""
folders=["/media/kitware/My Passport/twitter_USA/2013-05/","/media/kitware/My Passport/twitter_USA/2013-10/"]

for folder in folders:
    fCount=0
    for filename in os.listdir(folder):
        dayCount=0
        with open(folder+filename,"r") as tf:
            for line in tf.readlines():
                dayCount+=1
                fCount+=1
        print filename+": "+ str(dayCount)
    print folder+": "+str(fCount)

