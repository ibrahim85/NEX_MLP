# -*- coding: utf-8 -*-
import gzip
import json
import carmen

locfile=open("../data/realTwitter/testLocationChek.txt","a+")
count=8478
totalcount=502764
with gzip.open("/home/kitware/aalim/data/Twitter/tweets.2013-05-01T00%3A00.M=000.gz","rb") as tf:
    for i,line in enumerate(tf.readlines()):

        totalcount+=1
        if i>=502764:
            print line
            tweet=json.loads(line)

            if tweet.has_key("delete"):
                continue

            if tweet['geo']==None and tweet["place"]==None and tweet["coordinates"]==None:

                continue
            #for key,value in tweet.items():
            #    print key,value

            count+=1
            resolver = carmen.get_resolver()
            resolver.load_locations()
            location = resolver.resolve_tweet(tweet)
            print"-----------------"+str(count)+"/"+str(totalcount)+"----------------\n"
            print(location)
            print(tweet['geo'],tweet["place"],tweet["coordinates"])
            print(json.dumps(tweet, indent=4))
            locfile.write(str(location)+"\n")

            keys_list=tweet.keys()
            #for key,value in tweet.items():
            #    print key,value
        else:
            break
print(str(count)+"/"+str(totalcount))
