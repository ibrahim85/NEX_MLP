# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 17:10:04 2016

@author: kitware
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 04 12:47:36 2016

@author: adil.alim
"""
from random import shuffle
import random
import numpy as np
from nltk.corpus import stopwords
try:
    import cPickle as pickle
except:
    import pickle
import pprint
import gc
import os,re
import TwitterSimuDataGen.chi as chi

stop_words=["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]


##################################################################################


def getFeatureVectorWithLabels(tweets, featureList):

    map = {}
    data=[]
    feature_vector = []
    labels = []
    for t in tweets:
        label = 0
        map = {}
        #Initialize empty map
        for w in featureList:
            map[w] = 0

        tweet_words = t[0]
        tweet_lablel = t[1]
        #Fill the map
        for word in tweet_words:
            #process the word (remove repetitions and punctuations)

            word = word.strip("'\"*?,.")
            #set map[word] to 1 if word exists
            if word in map:
                map[word] = 1
        #end for loop
        values = map.values()
        feature_vector.append(values)

        labels.append(tweet_lablel)
    data.append(feature_vector)
    data.append(labels)
    #return the list of feature_vector and labels
    return data

def get_Labeled_twitter(filename):
    tweets=[]
    countNone=0
    with open(filename) as tF:
        for line in tF.readlines():
            terms=line.split(",")
            if len(terms[1].split())>=2:
                tweets.append((terms[0],terms[1],terms[2]))
            else:
                countNone+=1
    return tweets

def get_Labeled_twitter_withoutID(filename):
    tweets=[]
    countNone=0
    with open(filename) as tF:
        for line in tF.readlines():
            terms=line.split(",")
            if len(terms[1].split())>=2:
                tweets.append((terms[1].split(),terms[2]))
            else:

                countNone+=1
    print "Tweets Count:"+str(len(tweets))
    return tweets

def get_Labeled_twitter_withoutID_balance(filename):
    tweets=[]
    countNone=0
    constrain=0
    with open(filename) as tF:
        for line in tF.readlines():
            terms=line.split(",")
            if len(terms[1].split())<2:
                continue

            if terms[2].strip()=="0":
                #print terms[2],type(terms[2])
                if constrain>2000:
                    continue
                else :
                    tweets.append((terms[1].split(), terms[2]))
                    constrain+=1
            else:
                tweets.append((terms[1].split(), terms[2]))

    print "Tweets Count:"+str(len(tweets))
    return tweets

def get_Words_WithFreq(twitter_train):
    word_freq={}
    lables=[]
    for tweet,label in twitter_train:
        lables.append(label)

        for word in tweet:

            word = word.strip('\'"?,*.')
            if word in stop_words and word not in stopwords.words('english') :
                continue
            if len(word)<=2:
                continue
            if word_freq.has_key(word):
                word_freq[word]+=1
            else:
                word_freq[word]=1
    wordlist=[]
    for i,word in enumerate(sorted(word_freq, key=word_freq.get, reverse=True)):
        #print i,word,word_freq[word]
        wordlist.append(word)

    lables=list(set(lables))
    catagory_count=len(lables)
    return wordlist,catagory_count



def main():


    """ data paths"""
    # "/media/kitware/My Passport/twitter_USA/2013-05_label/2013-05-01.txt"


    testDateFile='/media/kitware/My Passport/twitter_USA/2013-05_label/2013-05-13.txt'
    validDataFile= '/media/kitware/My Passport/twitter_USA/2013-05_label/2013-05-27.txt'

    """ Read Training Tweets, and extract the keywords(features), and Run CHI """
    twitter_train=[]
    for i in range(1,11):
        day='{0:02d}'.format(i)
        trainDataFile = '/media/kitware/My Passport/twitter_USA/2013-05_label/2013-05-'+str(day)+'.txt'
        twitter_train.extend(get_Labeled_twitter_withoutID_balance(trainDataFile))


    wordlist,catagory_count=get_Words_WithFreq(twitter_train)
    wordlist=chi.CHI(twitter_train,catagory_count,wordlist)

    Fea_N=len(wordlist)

    print 'Feature number',len(wordlist)
    print wordlist

    import zipfile,time

    TVT=["train","valid","test"]
    fileName=["RealTwitter_Features" + str(Fea_N) + "_" + i + ".pkl" for i in TVT]

    t0=time.time()

    trainData =getFeatureVectorWithLabels(twitter_train,wordlist)
    print len(trainData),type(trainData),type(trainData[0]),type(trainData[0][0]),type(trainData[0][0][0]),
    twitter_train=[]
    with open("data/realTwitter/"+fileName[0],"w") as trd:
        pickle.dump(trainData,trd)
    print 'Train data is Done...'

    ''' Validate data  '''
    twitter_valid = get_Labeled_twitter_withoutID_balance(testDateFile)
    validData =getFeatureVectorWithLabels(twitter_valid,wordlist)
    twitter_valid=[]
    with open("data/realTwitter/"+fileName[1],"w") as trd:
        pickle.dump(validData,trd)
    print 'Validate data is Done...'

    ''' Testing data  '''
    twitter_test = get_Labeled_twitter_withoutID_balance(validDataFile)
    testData =getFeatureVectorWithLabels(twitter_test,wordlist)
    twitter_testing=[]
    with open("data/realTwitter/"+fileName[2],"w") as trd:
        pickle.dump(testData,trd)
    print 'Test data is Done...'


    t1=time.time()
    print "finsihed dumping",t1-t0," sec..."
    for i in range(3):
        with zipfile.ZipFile("data/realTwitter/"+fileName[i]+".zip", 'w', zipfile.ZIP_DEFLATED, allowZip64 = True) as myzip:
            myzip.write("data/realTwitter/"+fileName[i])
            os.remove("data/realTwitter/"+fileName[i])
    print "finihsed zipping",time.time()-t1," sec..."




if __name__ == '__main__':
    main()