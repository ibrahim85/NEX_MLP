# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 13:28:48 2016

@author: kitware
"""
from __future__ import print_function
import numpy as np
from nltk.corpus import stopwords
import time

stop_words=["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]


def CHI(twitter,catagory,terms):


    """ Generate Term Dictionary... """
    term_idx={}
    idx_term={}
    count=0
    for term in terms:
        if term not in stop_words and term not in stopwords.words('english') :
            term_idx[term]=count
            idx_term[count]=term
            count+=1

    N_c = catagory      # number of catagory
    N = len(twitter)    # number of twitter
    N_t = len(term_idx) # number of terms(unique words)
    print(N, N_c, N_t)

    two_way_contigency=np.zeros((N_t,N_c))
    for i,(tweet,label) in enumerate(twitter):
        print("\r{0}".format(i)),
        for word in tweet:
            word = word.strip('\'"?*,.')
            if word not in idx_term.values() or len(word)<=2:
                # if word in stop_words or word in stopwords.words('english'):
                #     print word," is stopword"
                # else:
                #     print word,"not in...."
                continue
            # if len(word)<=2:
            #     print "short word..."
            #     continue
            #print word, tweet, term_idx[word], label
            two_way_contigency[int(term_idx[word])][int(label)]+=1


    X2=np.zeros((N_t,N_c))
    for i in range(N_t):
        print("term ID ",i)
        for j in range(N_c):
            A=two_way_contigency[i][j]
            B=np.sum(two_way_contigency,axis=1)[i]-A
            C=np.sum(two_way_contigency,axis=0)[j]-A
            D=np.sum(two_way_contigency)-(B+C)-A
            term1=N*(A*D-C*B)*(A*D-C*B)
            term2=(A+C)*(B+D)*(A+B)*(C+D)
            #print term1,term2
            X2[i][j]=term1/term2
    idx=[]
    word_cut=100
    #np.argsort(X2[:,i])[-3:])
    for i in range(N_c):
        idx.extend(np.argsort(X2[:,i])[-word_cut:])
    print(N_t,len(term_idx))
    print(len(idx),len(list(set(idx))))

    selected_features=[]
    for i in list(set(idx)):
        print(idx_term[i])
        selected_features.append(idx_term[i])

    return selected_features
