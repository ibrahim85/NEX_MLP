# -*- coding: utf-8 -*-


import carmen,os,gzip,json

locfile=open("../data/realTwitter/testLocationChek.txt","a+")
count=0
totalcount=0



with gzip.open("/home/kitware/aalim/data/Twitter/tweets.2013-05-01T00%3A00.M=000.gz","rb") as tf:
    for i,line in enumerate(tf.readlines()):

        totalcount+=1
        if i<=200:
            #print line
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
            #print(json.dumps(tweet, indent=4))
            locfile.write(str(location)+"\n")
            place=dict(tweet["place"])
            print(place['full_name'].split(",")[0]+" "+place['full_name'].split(",")[1]+" "+place['country'])
            #keys_list=tweet.keys()
            #for key,value in tweet.items():
            #    print key,value
        else:
            break
print(str(count)+"/"+str(totalcount))
