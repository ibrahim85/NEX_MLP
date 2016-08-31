# -*- coding: utf-8 -*-

import gzip
import json
import carmen,os
from multiprocessing import Pool
import time
import json, requests


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
                    label,location = resolver.resolve_tweet(tweet)
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
Fcount=0
def main_singleFileFN(fileName):
    #print(fileName)
    global Fcount
    count=0
    totalcount=0
    t0=time.time()
    print("processing: "+fileName.split("/")[-1])
    with open("/media/kitware/My Passport/twitter_USA/"+fileName.split("/")[-2]+"/"+((fileName.split("/")[-1]).split("T")[0]).split(".")[1]+".txt","a+") as locfile:
        with open(fileName,"rb") as tf:
            for i,line in enumerate(tf.readlines()):
                line=line.strip()
                if len(line.strip())<1 and not line:
                    break
                else:

                    if i>=0:
                        try:
                            tweet=json.loads(line)

                        except:
                            print "exp:--",i,line
                            continue
                        totalcount+=1
                        if tweet.has_key("delete"):
                            continue
                        if tweet.get('geo')==None and tweet.get("place")==None and tweet.get("coordinates")==None:
                            print "@@@\n,@@@\n,@@@\n,@@@\n,@@@\n,@@@\n"
                            continue
                        if tweet.get("place")!=None:
                            if tweet.get("place")["country"]=="United States":
                                locfile.write(line+"\n")
                                count+=1
                        else:
                            if tweet.get('geo')!=None:
                                coord=tweet.get('geo')["coordinates"]
                            elif tweet.get("coordinates")!=None:
                                coord=tweet.get('coordinates')["coordinates"]
                            #print coord
                            geo_code=str(coord[0])+","+str(coord[1])
                            url="http://localhost:8081/geocoder.html?ll="+geo_code
                            resp = requests.get(url)
                            if len(resp.json()['interpretations'])>0:
                                cityFeat=dict(dict(resp.json()['interpretations'][-1])['feature'])['name']
                                if str(cityFeat)=="United States":
                                    locfile.write(line+"\n")
                                    print ">>>",cityFeat
                                    count+=1

                            else:
                                continue



                    else:
                        break
    Fcount+=1

    print("##########################################\n"+str(Fcount)+" "+fileName.split("/")[-1]+"  "+str(count)+"/"+str(totalcount)+"\n##########################################\n")
    print(time.time()-t0," sec...")
    return str(count)+"/"+str(totalcount)


if __name__ == "__main__":
    file_list=[]
    folders=["/media/kitware/My Passport/twitterWithGeoInfo/2013-05/","/media/kitware/My Passport/twitterWithGeoInfo/2013-10/"]
    for i,folder in enumerate(folders[1:]):
        for j,filename in enumerate(os.listdir(folder)):
            if i>=0:
                main_singleFileFN(folder+filename)



# -*- coding: utf-8 -*-

