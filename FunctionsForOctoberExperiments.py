#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'velazquezerick'
import itertools
from itertools import *
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk import word_tokenize
from collections import Counter
from string import lower
import math
import glob
import codecs

englishStopWords = stopwords.words('english')
toker = RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True)
bnc_ic = wordnet_ic.ic('ic-bnc.dat')

def getNameFiles(path):
    return glob.glob(path)

def readSingleFile (vectorFileName):
    filesContent = []
    for nameFile in vectorFileName:
        f = codecs.open(nameFile, mode= 'rt', encoding='utf-8')
        single_file = []
        for line in f:
            single_file.append(line)
        filesContent.append(single_file)
        f.close()

    return filesContent

def eliminateStopWords(docS):
    nDoc = []
    for p in docS:
        nParagraph = []
        for s in p:
            tokenizedS = toker.tokenize(s)
            nVector = [w.lower() for w in tokenizedS if w.lower() not in englishStopWords]
            nT = list(set(nVector))
            nParagraph.append(nT)
        nDoc.append(nParagraph)

    return nDoc

def transformParagraphIntoOneSentenceFormat(documents):

    nDoc = []
    for pa in documents:
        npa = []
        for s in pa:
            for w in s:
                npa.append(w)
        nDoc.append(npa)
    return nDoc

def calculate_idf(corpus):

    list_of_words = set(itertools.chain.from_iterable(corpus))
    idf = {}
    for w in list(list_of_words):
        cw = 0.0
        for c in corpus:
            if w in set(c):
                cw = cw + 1
        idf[w] = len(corpus)/ cw
    return idf

def myCalculate_idf(corpus):
    idf = {}
    listOfTerms =[]
    for p in corpus:
        for w in p:
            listOfTerms.append(w)
    wordCounted = Counter(imap(lower,listOfTerms))

    for k in wordCounted.keys():
        if wordCounted[k] >0:
            val = math.log((len(corpus)/float(wordCounted[k])),10)
            idf[k] = val
    return idf

#Addison Woolsey
def maxSim(w1, texte):
    #print 'is this used'
    syn1 = wn.synsets(w1)
    if len(syn1) == 0 : return 0
    c1 = syn1[0]  # we are taking the first element of the synset.
    if not (c1.pos() in ['n', 'v']): return 0 # testing only nouns and verbs
    mxsim = 0.0
    for w2 in texte:
        syn2 = wn.synsets(w2)
        if len(syn2) == 0 : continue
        c2 = syn2[0]
        if not (c2.pos in ['n', 'v']): continue # testing only nouns and verbs
        if c1.pos != c2.pos: continue  # the part-of-speech category has to be the same
        s = c1.lin_similarity(c2, bnc_ic)
        if s > mxsim:
            mxsim = s
    return mxsim
#
#
def maxSim2(w1, texte):
    #print 'max2'
    mxsim = 0.0
    mxconcept = "***"
    #print w1
    syn1 = wn.synsets(w1)
    #print 'desde maxSim2', len(syn1)
    if len(syn1) == 0 : return [mxsim, mxconcept]
    c1 = syn1[0]  # we are taking the first element of the synset.
    #print c1.pos
    # for my computer
    #if not (c1.pos in ['n', 'v']): return [mxsim, mxconcept] # testing only nouns and verbs
    #print type(c1.pos)
    if not (c1.pos in ['n', 'v']): return [mxsim, mxconcept] # testing only nouns and verbs
    for w2 in texte:
        #print 'entra al for'
        syn2 = wn.synsets(w2)
        if len(syn2) == 0 : continue
        c2 = syn2[0]
        if not (c2.pos in ['n', 'v']): continue # testing only nouns and verbs
        if c1.pos != c2.pos: continue  # the part-of-speech category has to be the same
        s = c1.lin_similarity(c2, bnc_ic)
        #print s
        if s > mxsim:
            mxsim = s
            mxconcept = w2
    return [mxsim, mxconcept]
#
def sim(txt1, txt2, idf1, idf2):
    t1 = 0.0
    d1 = 0.0
    for w in txt1:
        t1 = t1 + maxSim(w, txt2) * idf1[w]
        d1 = d1 + idf1[w]
    t1 = t1 / d1
    t2 = 0.0
    d2 = 0.0
    for w in txt2:
        t2 = t2 + maxSim(w, txt1) * idf2[w]
        d2 = d2 + idf2[w]
    t2 = t2 / d2
    return (t1 + t2)/2.0
#
def sim2(referent, subject, idf1):

    #print subject
    t1 = 0.0
    d1 = 0.0
    max1 = 0.0
    maxcon1 = "***"
    for w in referent:
        ms = maxSim2(w, subject)
        t1 = t1 + ms[0] * idf1[w]
        d1 = d1 + idf1[w]
        if ms[0] > max1:
            max1 = ms[0]
            maxcon1 = ms[1]
    if t1 == 0 or d1 ==0:
        t1 = 0
    else:
        t1 = t1 / d1

    return [t1, maxcon1]
def selectTheBestSimilarityValue(referent, subject, idf_referent):
    #selectTheBestSimilarityValue(paragraphStudent, textProfessor, idf_student)
    maxSim = 0
    indexM = -1
    term = '***'
    i = 0

    while i < len(subject):
        para = subject[i]
        sim = sim2(referent, para,idf_referent)
        if sim[0] > maxSim:
            maxSim = sim[0]
            term = sim[1]
            indexM = i
        i = i + 1

    return maxSim, indexM, term

def selectTheBestSimilarityValue2(referent, subject, idf_referent):
    #selectTheBestSimilarityValue(paragraphStudent, textProfessor, idf_student)
    maxSim = 0
    indexM = -1
    term = '***'
    i = 0

    while i < len(referent):
        para = referent[i]
        sim = sim2(referent, para,idf_referent)
        if sim[0] > maxSim:
            maxSim = sim[0]
            term = sim[1]
            indexM = i
        i = i + 1

    return maxSim, indexM, term
