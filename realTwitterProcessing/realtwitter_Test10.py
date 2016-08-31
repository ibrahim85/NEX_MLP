# -*- coding: utf-8 -*-
"""
Created on Sat Aug 06 22:30:02 2016

@author: Adil
"""

# -*- coding: utf-8 -*-
import gzip
import json
import carmen,os
from multiprocessing import Pool
import time
Fcount=0

def main_singleFile():
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
                print(json.dumps(tweet, indent=4))
                locfile.write(str(location)+"\n")

                #keys_list=tweet.keys()
                for key,value in tweet.items():
                    print key,value
            else:
                break
    print(str(count)+"/"+str(totalcount))


def oneDayTest():

    locfile=open("../data/realTwitter/testLocationChek.txt","a+")
    loc_day=0
    total_day=0


    for filename in os.listdir("/home/kitware/aalim/data/Twitter/"):
        print "Processing File "+filename
        count=0
        totalcount=0
        with gzip.open("/home/kitware/aalim/data/Twitter/"+filename,"rb") as tf:
            for i,line in enumerate(tf.readlines()):

                totalcount+=1
                if i>=0:

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
                    print"<=="+filename.split("%")[0]+" .... "+str(count)+"/"+str(totalcount)
                    #print(location,tweet['geo'],tweet["place"],tweet["coordinates"])
                    #print(json.dumps(tweet, indent=4))
                    locfile.write(str(location)+"\n")


                    #keys_list=tweet.keys()
                    #for key,value in tweet.items():
                    #    print key,value
                else:
                    break
            print(str(count)+"/"+str(totalcount))

            loc_day+=count
            total_day+=totalcount
            locfile.write(str(location)+"\n")
    print(str(count)+"/"+str(totalcount))

def oneDayTest_revised():

    locfile=open("../data/realTwitter/testLocationChek.txt","a+")
    loc_day=0
    total_day=0
    global Fcount

    for filename in os.listdir("/home/kitware/aalim/data/Twitter/"):
        print "Processing File "+filename
        count=0
        totalcount=0
        with gzip.open("/home/kitware/aalim/data/Twitter/"+filename,"rb") as tf:
            for i,line in enumerate(tf.readlines()):

                totalcount+=1
                if i>=0:

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
                    print"<=="+filename.split("%")[0]+" .... "+str(count)+"/"+str(totalcount)
                    #print(location,tweet['geo'],tweet["place"],tweet["coordinates"])
                    #print(json.dumps(tweet, indent=4))
                    locfile.write(str(location)+"\n")


                    #keys_list=tweet.keys()
                    #for key,value in tweet.items():
                    #    print key,value
                else:
                    break
            print(str(count)+"/"+str(totalcount))
            Fcount+1
            loc_day+=count
            total_day+=totalcount
            locfile.write(str(location)+"\n")
    print(str(count)+"/"+str(totalcount))
    return str(count)+"/"+str(totalcount)

def main_singleFileFN(fileName):
    #print(fileName)
    global Fcount
    count=0
    totalcount=0
    t0=time.time()
    print("processing: "+fileName.split("/")[-1])
    with open("/media/kitware/My Passport/"+fileName.split("/")[-2]+"/"+".".join((fileName.split("/")[-1]).split(".")[:-1])+".txt","w") as locfile:
        with gzip.open(fileName,"rb") as tf:
            for i,line in enumerate(tf.readlines()):
                line=line.strip()
                if len(line.strip())<1 and not line:
                    break
                else:
                    totalcount+=1
                    if i>=0:
                        try:
                            tweet=json.loads(line)
                        except:
                            print line
                            continue

                        if tweet.has_key("delete"):
                            continue

                        if tweet.get('geo')==None and tweet.get("place")==None and tweet.get("coordinates")==None:

                            continue

                        #print(fileName.split("/")[-1]+str(count)+"/"+str(totalcount))
                        count+=1
                        locfile.write(line+"\n")

                    else:
                        break
    Fcount+=1

    print("##########################################\n"+str(Fcount)+" "+fileName.split("/")[-1]+"  "+str(count)+"/"+str(totalcount)+"\n##########################################\n")
    print(time.time()-t0," sec...")
    return str(count)+"/"+str(totalcount)


if __name__ == "__main__":
    file_list=[]
    folders=["/media/kitware/My Passport/twitter/2013-05/boston.lti.cs.cmu.edu/twitter_data/twitter_corpus/2013-05/","/media/kitware/My Passport/twitter/2013-10/boston.lti.cs.cmu.edu/twitter_data/twitter_corpus/2013-10/"]
    #folders=["G:/twitter/2013-05/boston.lti.cs.cmu.edu/twitter_data/twitter_corpus/2013-05/","G:/twitter/2013-10/boston.lti.cs.cmu.edu/twitter_data/twitter_corpus/2013-10/"]
    mon=["2013-05-","2013-10-"]

    dfl=[]
    #for filename in os.listdir("/media/kitware/My Passport/2013-100/"):
    #    dfl.append(".".join(filename.split(".")[:-1])+".gz")

    for i,folder in enumerate(folders[1:]):

        for filename in os.listdir(folder):
            if filename.startswith("t") and ((filename.split("/")[-1]).split("T")[0]).split(".")[1]=="2013-10-31":
                #print(filename)
                file_list.append(filename)
                main_singleFileFN(folder+filename)


#        print(i,mon[i])
#        #for filename in os.listdir("/home/kitware/aalim/data/Twitter/"):
#        monStr=mon[i]
#        days=["%02d"%(i,) for i in range(1,32)]
#        hours=["%02d"%(i,) for i in range(24)]
#        minus=['00','15','30','45']
#        for day in days:
#            for hour in hours:
#                for minu in minus:
#
#                    fileName=folder+"tweets."+monStr+day+"T"+hour+"%3A"+minu+".M=000.gz"
#                    main_singleFileFN(fileName)
#        #oneDayTest()
#        #main_singleFile()






