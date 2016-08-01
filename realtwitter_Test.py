# -*- coding: utf-8 -*-
import gzip
import json


with gzip.open("/home/kitware/aalim/data/Twitter/tweets.2013-05-01T00%3A00.M=000.gz","rb") as tf:
    for i,line in enumerate(tf.readlines()):
        #print line
        if i<10:
            twitter=json.loads(line)
            print twitter.keys()
        else:
            break
