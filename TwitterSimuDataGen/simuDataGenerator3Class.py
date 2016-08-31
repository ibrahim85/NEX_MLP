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
import os,re
import chi

stop_words=["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

wh_wordlist=[]
with open("data/wHot.txt") as wf:
    for line in wf.readlines():
        line=re.sub('[^\w]', ' ',line)
        if len(line.strip('\'"?,.').split())>1:
            wh_wordlist.extend(line.strip().split())
        wh_wordlist.append(line.strip())

wc_wordlist=[]
with open("data/wCold.txt") as wf:
    for line in wf.readlines():
        line=re.sub('[^\w]', ' ',line)
        if len(line.strip().split())>1:
            wc_wordlist.extend(line.strip().split())
        wc_wordlist.append(line.strip())



w_wordlist=wh_wordlist+wc_wordlist
random_wordlist=[]
with open("data/words.txt") as rf:
    for line in rf.readlines():
        line=re.sub('[^\w]', ' ',line)

        if len(line.split())>1:
            for word in line.split():
                if len(word)>2:
                    random_wordlist.append(word)
        else:
            word=line.strip().replace("\n","")
            if word not in stop_words and word not in w_wordlist:
                random_wordlist.append(word)
            #print word
        #else:
            #print word

w_wordlist+=random.sample(random_wordlist,200)

print len(stop_words),len(random_wordlist),"\n",len(w_wordlist)
#print w_wordlist

k=1000
twitter_train=[]


for i in range(int(2.5*k)):
    temp=[]
    temp.extend(random.sample(wh_wordlist,(np.random.binomial(5,0.5,1)+1)[0]))
    temp.extend(random.sample(random_wordlist,np.random.binomial(15,0.5,1)[0]))
    random.shuffle(temp,random.random)
    twitter_train.append((temp,1))

    temp=[]
    temp.extend(random.sample(wc_wordlist,(np.random.binomial(5,0.5,1)+1)[0]))
    temp.extend(random.sample(random_wordlist,np.random.binomial(20,0.5,1)[0]))
    random.shuffle(temp,random.random)
    twitter_train.append((temp,2))




for i in range(90*k):
    temp=[]
    temp.extend(random.sample(random_wordlist,np.random.binomial(25,0.5,1)[0]))
    random.shuffle(temp,random.random)
    twitter_train.append((temp,0))

random.shuffle(twitter_train,random.random)
pickle.dump(twitter_train, open("data/train.pkl","w"))
gc.collect()

twitter_verify=[]


for i in range(int(2.5*k)):
    temp=[]
    temp.extend(random.sample(wh_wordlist,(np.random.binomial(5,0.5,1)+1)[0]))
    temp.extend(random.sample(random_wordlist,np.random.binomial(15,0.5,1)[0]))
    random.shuffle(temp,random.random)
    twitter_verify.append((temp,1))

    temp=[]
    temp.extend(random.sample(wc_wordlist,(np.random.binomial(5,0.5,1)+1)[0]))
    temp.extend(random.sample(random_wordlist,np.random.binomial(20,0.5,1)[0]))
    random.shuffle(temp,random.random)
    twitter_verify.append((temp,2))

for i in range(9*k):
    temp=[]
    temp.extend(random.sample(random_wordlist,np.random.binomial(20,0.5,1)[0]))
    random.shuffle(temp,random.random)
    twitter_verify.append((temp,0))

random.shuffle(twitter_verify,random.random)
pickle.dump(twitter_verify, open("data/verify.pkl","w"))
gc.collect()


twitter_testing=[]


for i in range(int(0.5*k)):
    temp=[]
    temp.extend(random.sample(wh_wordlist,(np.random.binomial(5,0.5,1)+1)[0]))
    temp.extend(random.sample(random_wordlist,np.random.binomial(15,0.5,1)[0]))
    random.shuffle(temp,random.random)
    twitter_testing.append((temp,1))

    temp=[]
    temp.extend(random.sample(wc_wordlist,(np.random.binomial(5,0.5,1)+1)[0]))
    temp.extend(random.sample(random_wordlist,np.random.binomial(20,0.5,1)[0]))
    random.shuffle(temp,random.random)
    twitter_testing.append((temp,2))

for i in range(9*k):
    temp=[]
    temp.extend(random.sample(random_wordlist,np.random.binomial(20,0.5,1)[0]))
    random.shuffle(temp,random.random)
    twitter_testing.append((temp,0))


random.shuffle(twitter_testing,random.random)
pickle.dump(twitter_testing, open("data/test.pkl","w"))
gc.collect()


#tweets=twitter_testing+ twitter_train+twitter_verify
wordlist=[]
word_freq={}
lables=[]
for tweet,label in twitter_train:
    lables.append(label)
    for word in tweet:

        word = word.strip('\'"?,.')
        if word in stop_words:
            continue
        if len(word)<=2:
            continue
        if word_freq.has_key(word):
            word_freq[word]+=1
        else:
            word_freq[word]=1
lables=list(set(lables))
catagory=len(lables)
for i,word in enumerate(sorted(word_freq, key=word_freq.get, reverse=True)):
    print i,word,word_freq[word]
    wordlist.append(word)
print 'Intersection:',list(set(wordlist) & set(wh_wordlist+wc_wordlist))
wordlist=chi.CHI(twitter_train,3,wordlist)
#print len(w_wordlist)
#
#for word in w_wordlist:
#    word = word.strip('\'"?,.')
#    wordlist.append(word)
#wordlist=sorted(list(set(wordlist)))

print 'Feature number',len(wordlist)
Fea_N=len(wordlist)
tweets=[]
print 'Twitter Generation is Done....'
gc.collect()
##################################################################################


def getFeatureVectorWithLabels(tweets, featureList):

    map = {}
    data=[]
    feature_vector = []
    labels = []
    for t in tweets:

        map = {}
        #Initialize empty map
        for w in featureList:
            map[w] = 0.0

        tweet_words = t[0]
        tweet_lablel = t[1]
        #Fill the map
        for word in tweet_words:
            #process the word (remove repetitions and punctuations)

            word = word.strip('\'"?,.')
            #set map[word] to 1 if word exists
            if word in map:
                map[word] = 1.0
        #end for loop
        values = map.values()
        feature_vector.append(values)

        labels.append(tweet_lablel)
    data.append(feature_vector)
    data.append(labels)
    #return the list of feature_vector and labels
    return data



import zipfile,time

TVT=["train","verify","test"]
fileName=["simuTW_3Class_HighFea"+str(Fea_N)+"_K"+str(k)+"_"+i+".pkl" for i in TVT]
t0=time.time()
###  Training data  ###
with open("data/train.pkl","rb") as tr:
    twitter_train=pickle.load(tr)
trainData =getFeatureVectorWithLabels(twitter_train,wordlist)
print len(trainData),type(trainData),type(trainData[0]),type(trainData[0][0]),type(trainData[0][0][0]),
twitter_train=[]
with open("data/"+fileName[0],"w") as trd:
    pickle.dump(trainData,trd)
print 'Train data is Done...'

### Validate data  ###
with open("data/verify.pkl","rb") as tr:
    twitter_verify=pickle.load(tr)
veriryData =getFeatureVectorWithLabels(twitter_verify,wordlist)
twitter_verify=[]
with open("data/"+fileName[1],"w") as trd:
    pickle.dump(veriryData,trd)
print 'Validate data is Done...'

### Testing data  ###
with open("data/test.pkl","rb") as tr:
    twitter_testing=pickle.load(tr)
testData =getFeatureVectorWithLabels(twitter_testing,wordlist)
twitter_testing=[]
with open("data/"+fileName[2],"w") as trd:
    pickle.dump(testData,trd)
print 'Test data is Done...'





os.remove("data/train.pkl")
os.remove("data/test.pkl")
os.remove("data/verify.pkl")





t1=time.time()
print "finsihed dumping",t1-t0," sec..."
for i in range(3):
    with zipfile.ZipFile("../NEX_MLP/data/simuData/"+fileName[i]+".zip", 'w', zipfile.ZIP_DEFLATED, allowZip64 = True) as myzip:
        myzip.write("data/"+fileName[i])
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
