# -*- coding: utf-8 -*-
"""
Created on Mon Jul 04 12:47:36 2016

@author: adil.alim
"""
from random import shuffle
import random
import numpy as np
try:
    import cPickle as pickle
except:
    import pickle
import pprint
import gc
import os

#stop_words=["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]
#
#wh_wordlist=[]
#with open("wHot.txt") as wf:
#    for line in wf.readlines():
#        if len(line.strip().split())>1:
#            wh_wordlist.extend(line.strip().split())
#        wh_wordlist.append(line.strip())
#
#wc_wordlist=[]
#with open("wCold.txt") as wf:
#    for line in wf.readlines():
#        if len(line.strip().split())>1:
#            wc_wordlist.extend(line.strip().split())
#        wc_wordlist.append(line.strip())
#
#
#
#w_wordlist=wh_wordlist+wc_wordlist
#random_wordlist=[]
#with open("words.txt") as rf:
#    for line in rf.readlines():
#        word=line.strip().replace("\n","")
#        if len(line.strip().split())>1:
#            random_wordlist.extend(line.strip().split())
#        if word not in stop_words and word not in w_wordlist:
#            random_wordlist.append(word)
#            #print word
#        #else:
#            #print word
#w_wordlist+=random.sample(random_wordlist,300)
#
#print len(stop_words),len(random_wordlist),"\n",len(w_wordlist)
##print w_wordlist
#
#k=5000
#twitter_train=[]
#
#
#for i in range(int(2.5*k)):
#    temp=[]
#    temp.extend(random.sample(wh_wordlist,(np.random.binomial(5,0.5,1)+1)[0]))
#    temp.extend(random.sample(random_wordlist,np.random.binomial(15,0.5,1)[0]))
#    random.shuffle(temp,random.random)
#    twitter_train.append((temp,1))
#
#    temp=[]
#    temp.extend(random.sample(wc_wordlist,(np.random.binomial(5,0.5,1)+1)[0]))
#    temp.extend(random.sample(random_wordlist,np.random.binomial(20,0.5,1)[0]))
#    random.shuffle(temp,random.random)
#    twitter_train.append((temp,2))
#
#
#
#
#for i in range(90*k):
#    temp=[]
#    temp.extend(random.sample(random_wordlist,np.random.binomial(25,0.5,1)[0]))
#    random.shuffle(temp,random.random)
#    twitter_train.append((temp,0))
#
#random.shuffle(twitter_train,random.random)
#pickle.dump(twitter_train, open("train.pkl","w"))
#gc.collect()
#
#twitter_verify=[]
#
#
#for i in range(int(0.5*k)):
#    temp=[]
#    temp.extend(random.sample(wh_wordlist,(np.random.binomial(5,0.5,1)+1)[0]))
#    temp.extend(random.sample(random_wordlist,np.random.binomial(15,0.5,1)[0]))
#    random.shuffle(temp,random.random)
#    twitter_verify.append((temp,1))
#
#    temp=[]
#    temp.extend(random.sample(wc_wordlist,(np.random.binomial(5,0.5,1)+1)[0]))
#    temp.extend(random.sample(random_wordlist,np.random.binomial(20,0.5,1)[0]))
#    random.shuffle(temp,random.random)
#    twitter_verify.append((temp,2))
#
#for i in range(9*k):
#    temp=[]
#    temp.extend(random.sample(random_wordlist,np.random.binomial(20,0.5,1)[0]))
#    random.shuffle(temp,random.random)
#    twitter_verify.append((temp,0))
#
#random.shuffle(twitter_verify,random.random)
#pickle.dump(twitter_verify, open("verify.pkl","w"))
#gc.collect()
#
#
#twitter_testing=[]
#
#
#for i in range(int(0.5*k)):
#    temp=[]
#    temp.extend(random.sample(wh_wordlist,(np.random.binomial(5,0.5,1)+1)[0]))
#    temp.extend(random.sample(random_wordlist,np.random.binomial(15,0.5,1)[0]))
#    random.shuffle(temp,random.random)
#    twitter_testing.append((temp,1))
#
#    temp=[]
#    temp.extend(random.sample(wc_wordlist,(np.random.binomial(5,0.5,1)+1)[0]))
#    temp.extend(random.sample(random_wordlist,np.random.binomial(20,0.5,1)[0]))
#    random.shuffle(temp,random.random)
#    twitter_testing.append((temp,2))
#
#for i in range(9*k):
#    temp=[]
#    temp.extend(random.sample(random_wordlist,np.random.binomial(20,0.5,1)[0]))
#    random.shuffle(temp,random.random)
#    twitter_testing.append((temp,0))
#
#
#random.shuffle(twitter_testing,random.random)
#pickle.dump(twitter_testing, open("test.pkl","w"))
#gc.collect()
#
#
##tweets=twitter_testing+ twitter_train+twitter_verify
#wordlist=[]
#
#
#print len(w_wordlist)
#for word in w_wordlist:
#    word = word.strip('\'"?,.')
#    wordlist.append(word)
#wordlist=sorted(list(set(wordlist)))
#print 'Feature number',len(wordlist)
#tweets=[]
#print 'Twitter Generation is Done....'
#gc.collect()
###################################################################################
#
#
#def getFeatureVectorWithLabels(tweets, featureList):
#
#    map = {}
#    data=[]
#    feature_vector = []
#    labels = []
#    for t in tweets:
#        label = 0
#        map = {}
#        #Initialize empty map
#        for w in featureList:
#            map[w] = 0
#
#        tweet_words = t[0]
#        tweet_lablel = t[1]
#        #Fill the map
#        for word in tweet_words:
#            #process the word (remove repetitions and punctuations)
#
#            word = word.strip('\'"?,.')
#            #set map[word] to 1 if word exists
#            if word in map:
#                map[word] = 1
#        #end for loop
#        values = map.values()
#        feature_vector.append(values)
#
#        labels.append(tweet_lablel)
#    data.append(feature_vector)
#    data.append(labels)
#    #return the list of feature_vector and labels
#    return data
#
#
#
#import zipfile,time
#
#
fileName=["simuTW_3Class_300Fea_5000"+str(i)+".pkl" for i in range(1,4)]
#t0=time.time()
####  Training data  ###
#with open("train.pkl","rb") as tr:
#    twitter_train=pickle.load(tr)
#trainData =getFeatureVectorWithLabels(twitter_train,wordlist)
#twitter_train=[]
#with open(fileName[0],"w") as trd:
#    pickle.dump(np.asarray(trainData),trd)
#print 'Train data Done...'
#
#### Validate data  ###
#with open("train.pkl","rb") as tr:
#    twitter_verify=pickle.load(tr)
#veriryData =getFeatureVectorWithLabels(twitter_verify,wordlist)
#twitter_verify=[]
#with open(fileName[1],"w") as trd:
#    pickle.dump(np.asarray(veriryData),trd)
#print 'Validate data Done...'
#
#### Testing data  ###
#with open("train.pkl","rb") as tr:
#    twitter_testing=pickle.load(tr)
#testData =getFeatureVectorWithLabels(twitter_testing,wordlist)
#twitter_testing=[]
#with open(fileName[2],"w") as trd:
#    pickle.dump(np.asarray(testData),trd)
#print 'Test data Done...'
#
#
#
#
#
#os.remove("train.pkl")
#os.remove("test.pkl")
#os.remove("verify.pkl")





t1=time.time()
print "finsihed dumping",t1-t0," sec..."
for i in range(1,4):
    with zipfile.ZipFile("../handWritingEx/"+fileName[i-1]+".zip", 'w', zipfile.ZIP_DEFLATED, allowZip64 = True) as myzip:
        myzip.write(fileName[i-1])
print "finihsed zipping",time.time()-t1," sec..."



#fileName="twitterSimuData96Fea3Class500.json"
#t0=time.time()
#with open(fileName,"w") as jf:
#  json.dump(data,jf)
#t1=time.time()
#
#print "finsihed dumping",t1-t0," sec..."
#with zipfile.ZipFile("../handWritingEx/"+fileName+".zip", 'w', zipfile.ZIP_DEFLATED, allowZip64 = True) as myzip:
#    myzip.write(fileName)
#print "finihsed zipping",time.time()-t1," sec..."

#os.remove(fileName)
#print cPickle.load(open("twitterSimuData.pkl","rb"))
#print data
#print twitter
