# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 12:27:53 2016

@author: kitware
"""
import os,json
import ProcessTweets as PT
from nltk.stem import *
from nltk.corpus import stopwords
import time


def get_kw():
    hot_kw=[]
    cold_kw=[]
    with open("../data/wCold.txt") as cF:
        for line in cF.readlines():
            cold_kw.append(PT.wordStemming(line.strip()))

    with open("../data/wHot.txt") as hF:
        for line in hF.readlines():
            hot_kw.append(PT.wordStemming(line.strip()))

    return hot_kw,cold_kw

def get_label(tweet,hot_kw,cold_kw):
    # 0 for unrelated
    # 1 for hot
    # 2 for cold
    for word in tweet:
        if word in hot_kw:
            return 1
        elif word in cold_kw:
            return 2
        else:
            return 0




def main():
    hot_kw,cold_kw=get_kw()
    print hot_kw
    print cold_kw

    hot_labled=0
    cold_labled=0
    folders=["/media/kitware/My Passport/twitter_USA/2013-05/","/media/kitware/My Passport/twitter_USA/2013-10/"]
    label_folders=["/media/kitware/My Passport/twitter_USA/2013-05_label/","/media/kitware/My Passport/twitter_USA/2013-10_label/"]
    for k,folder in enumerate(folders[:1]):
        for i,filename in enumerate(os.listdir(folder)):
            label0=0
            label1=0
            label2=0
            label_file=open(label_folders[k]+filename,"a+")
            t1=time.time()
            with open(folder+filename,"rb") as tf:
                print filename,"------------------------------"
                for j,line in enumerate(tf.readlines()):
                    tweet_org=json.loads(line)
                    if i>=0 and j>=0:
                        #print "\n\n","(((",tweet['text']
                        tweet=PT.tweetStemming(tweet_org['text'])
                        if len(tweet)>=1:
                            label=get_label(tweet,hot_kw,cold_kw)
                        else:
                            continue
                        if label==0:
                            label0+=1
                        elif label==1:
                            label1+=1
                        else:
                            label2+=1
                        label_file.write(str(tweet_org['id'])+","+" ".join(tweet)+"," +str(label)+"\n")
                        #print "<<<",tweet_org['id'],tweet,label
                    else:
                        break


            print label0+label1+label2," Unrelated: ", label0,": HOT: ",label1,"  COLD: ",label2 ,time.time() - t1," Sec .."
            label_file.close()





if __name__ == '__main__':
    main()