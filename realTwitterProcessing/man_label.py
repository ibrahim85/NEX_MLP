# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 12:27:53 2016

@author: kitware
"""
import os,json
import ProcessTweets as PT
from nltk.stem import *
from nltk.corpus import stopwords
from random import shuffle
import time


def get_kw():
    kw=[]
    with open("../data/wKeywords.txt") as cF:
        for line in cF.readlines():
            kw.append(PT.wordStemming(line.strip()))
    return kw

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
def get_tweetID_list(fileName):
    id_list=[]
    with open(fileName,"r") as ft:
        for line in ft.readlines():
            id=int(line.split(",")[0])
            #print type(id),id
            id_list.append(id)
    return id_list

def is_related(tweet,kw):
    # 0 for unrelated
    # 1 for hot
    # 2 for cold
    for word in tweet:
        if word in kw:
            return 1
        else:
            return 0



def main():
    kw=get_kw()
    #print hot_kw
    #print cold_kw
    #print kw

    folders=["/media/kitware/My Passport/twitter_USA/2013-05/","/media/kitware/My Passport/twitter_USA/2013-10/"]
    label_folders=["/media/kitware/My Passport/twitter_USA/2013-05_man_label/","/media/kitware/My Passport/twitter_USA/2013-10_man_label/"]
    for k,folder in enumerate(folders[:1]):
        for i,filename in enumerate(os.listdir(folder)):
            label0=0
            label1=0
            label2=0
            label_file=open(label_folders[k]+filename,"a+")
            exist_tw_id_list=get_tweetID_list(label_folders[k]+filename)
            start_xount=len(exist_tw_id_list)
            print filename, "------------------------------"
            if start_xount>=4000:
                continue
            kw_related = []
            kw_unrelated = []
            t1=time.time()
            with open(folder+filename,"rb") as tf:

                for j,line in enumerate(tf.readlines()):
                    tweet_org=json.loads(line)
                    if i>=0 and j>=0:
                        #print "\n\n","(((",tweet['text']
                        tweet=PT.tweetStemming(tweet_org['text'])

                        tweet_id=tweet_org['id']


                        if len(tweet)>=1 and tweet_id not in exist_tw_id_list:
                            if is_related(tweet,kw)>0:
                                kw_related.append((tweet_id," ".join(tweet),tweet_org['text']))
                            else:
                                kw_unrelated.append((tweet_id," ".join(tweet),tweet_org['text']))

                        else:
                            continue

                    else:
                        break
            print "Key word related tweet:",len(kw_related)
            added_count=start_xount
            for i,t in enumerate(kw_related):
                tweet=""
                tweet=t[1]
                tweet_id=t[0]
                while True:
                    print added_count,t[2]
                    label = raw_input()

                    if label !=None and len(label)>0:
                        label=int(label)
                        if label in [0,1,2]:
                            break


                if label==0:
                    label0+=1
                elif label==1:
                    label1+=1
                else:
                    label2+=1


                added_count+=1
                if added_count>4000:
                    break
                label_file.write(str(tweet_id)+","+ tweet+","+ str(label)+"\n")
            shuffle(kw_unrelated)
            K=2000-label0
            print "---------------------------\nUnrelated #:",K
            for i,t in enumerate(kw_unrelated[:K]):
                tweet = t[1]
                tweet_id = t[0]
                while True:
                    print added_count,t[2]
                    label = raw_input()

                    if label !=None and len(label)>0:
                        label=int(label)
                        if label in [0,1,2]:
                            break

                if label == 0:
                    label0 += 1
                elif label == 1:
                    label1 += 1
                else:
                    label2 += 1
                added_count += 1
                if added_count > 4000:
                    break
                label_file.write(str(tweet_id) + "," + tweet + "," + str(label)+"\n")



            print label0+label1+label2," Unrelated: ", label0,": HOT: ",label1,"  COLD: ",label2 ,time.time() - t1," Sec .."
            label_file.close()





if __name__ == '__main__':
    main()