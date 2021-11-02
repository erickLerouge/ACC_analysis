#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'velazquezerick'

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from FunctionsForOctoberExperiments import getNameFiles
from FunctionsForOctoberExperiments import readSingleFile
from FunctionsForOctoberExperiments import eliminateStopWords
from FunctionsForOctoberExperiments import transformParagraphIntoOneSentenceFormat
from FunctionsForOctoberExperiments import myCalculate_idf
from FunctionsForOctoberExperiments import selectTheBestSimilarityValue

subject1Path = '/Users/velazquezerick/Dropbox/ERICK-PHD/2016/WeekNetherlands/Idea2/StudentCorpus/English/Student1/*.txt'
subject2Path = '/Users/velazquezerick/Dropbox/ERICK-PHD/2016/WeekNetherlands/Idea2/StudentCorpus/English/Student2/*.txt'
subject3Path = '/Users/velazquezerick/Dropbox/ERICK-PHD/2016/WeekNetherlands/Idea2/StudentCorpus/English/Student3/*.txt'
subject4Path = '/Users/velazquezerick/Dropbox/ERICK-PHD/2016/WeekNetherlands/Idea2/StudentCorpus/English/Student4/*.txt'


subjec1NameFiles = getNameFiles(subject1Path)
subjec2NameFiles = getNameFiles(subject2Path)
subjec3NameFiles = getNameFiles(subject3Path)
subjec4NameFiles = getNameFiles(subject4Path)

subject1 = readSingleFile(subjec1NameFiles )
subject2 = readSingleFile(subjec2NameFiles )
subject3 = readSingleFile(subjec3NameFiles )
subject4 = readSingleFile(subjec4NameFiles )

referent1Path = '/Users/velazquezerick/Dropbox/ERICK-PHD/2016/WeekNetherlands/Idea2/Referent1/TEXT/FinalBooks/Book1/*.txt'
referent2Path = '/Users/velazquezerick/Dropbox/ERICK-PHD/2016/WeekNetherlands/Idea2/Referent1/TEXT/FinalBooks/Book2/*.txt'
referent3Path = '/Users/velazquezerick/Dropbox/ERICK-PHD/2016/WeekNetherlands/Idea2/Referent1/TEXT/FinalBooks/Book3/*.txt'
referent4Path = '/Users/velazquezerick/Dropbox/ERICK-PHD/2016/WeekNetherlands/Idea2/Referent1/TEXT/FinalBooks/Book4/*.txt'
referent5Path = '/Users/velazquezerick/Dropbox/ERICK-PHD/2016/WeekNetherlands/Idea2/Referent1/TEXT/FinalBooks/Book5/*.txt'
referent6Path = '/Users/velazquezerick/Dropbox/ERICK-PHD/2016/WeekNetherlands/Idea2/Referent1/TEXT/FinalBooks/Book6/*.txt'
referent7Path = '/Users/velazquezerick/Dropbox/ERICK-PHD/2016/WeekNetherlands/Idea2/Referent1/TEXT/FinalBooks/Book7/*.txt'
referent8Path = '/Users/velazquezerick/Dropbox/ERICK-PHD/2016/WeekNetherlands/Idea2/Referent1/TEXT/FinalBooks/Book8/*.txt'
referent9Path = '/Users/velazquezerick/Dropbox/ERICK-PHD/2016/WeekNetherlands/Idea2/Referent1/TEXT/FinalBooks/Book9/*.txt'

#referentuPath = '/Users/velazquezerick/Dropbox/ERICK-PHD/2016/WeekNetherlands/Idea2/Referent2/Final1/*.txt'

referent1NameFiles = getNameFiles(referent1Path)
referent2NameFiles = getNameFiles(referent2Path)
referent3NameFiles = getNameFiles(referent3Path)
referent4NameFiles = getNameFiles(referent4Path)
referent5NameFiles = getNameFiles(referent5Path)
referent6NameFiles = getNameFiles(referent6Path)
referent7NameFiles = getNameFiles(referent7Path)
referent8NameFiles = getNameFiles(referent8Path)
referent9NameFiles = getNameFiles(referent9Path)

#referentuName_files = getNameFiles(referentuPath)

#print subject1
referent1 = readSingleFile(referent1NameFiles)
referent2 = readSingleFile(referent2NameFiles)
referent3 = readSingleFile(referent3NameFiles)
referent4 = readSingleFile(referent4NameFiles)
referent5 = readSingleFile(referent5NameFiles)
referent6 = readSingleFile(referent6NameFiles)
referent7 = readSingleFile(referent7NameFiles)
referent8 = readSingleFile(referent8NameFiles)
referent9 = readSingleFile(referent9NameFiles)

#referentu = readSingleFile(referentuName_files)

#print referent1
print 'Eliminate stopwords..'

subject1NoStopWords = eliminateStopWords(subject1)
subject2NoStopWords = eliminateStopWords(subject2)
subject3NoStopWords = eliminateStopWords(subject3)
subject4NoStopWords = eliminateStopWords(subject4)

allSubjectDocuments = []

allSubjectDocuments.append(transformParagraphIntoOneSentenceFormat(subject1NoStopWords))
allSubjectDocuments.append(transformParagraphIntoOneSentenceFormat(subject2NoStopWords))
allSubjectDocuments.append(transformParagraphIntoOneSentenceFormat(subject3NoStopWords))
allSubjectDocuments.append(transformParagraphIntoOneSentenceFormat(subject4NoStopWords))

documentReferent1NoStopWords = eliminateStopWords(referent1)
documentReferent2NoStopWords = eliminateStopWords(referent2)
documentReferent3NoStopWords = eliminateStopWords(referent3)
documentReferent4NoStopWords = eliminateStopWords(referent4)
documentReferent5NoStopWords = eliminateStopWords(referent5)
documentReferent6NoStopWords = eliminateStopWords(referent6)
documentReferent7NoStopWords = eliminateStopWords(referent7)
documentReferent8NoStopWords = eliminateStopWords(referent8)
documentReferent9NoStopWords = eliminateStopWords(referent9)

#documentReferentUNostopWords = eliminateStopWords(referentu)

allReferentDocuments = []

allReferentDocuments.append(transformParagraphIntoOneSentenceFormat(documentReferent1NoStopWords))
allReferentDocuments.append(transformParagraphIntoOneSentenceFormat(documentReferent2NoStopWords))
allReferentDocuments.append(transformParagraphIntoOneSentenceFormat(documentReferent3NoStopWords))
allReferentDocuments.append(transformParagraphIntoOneSentenceFormat(documentReferent4NoStopWords))
allReferentDocuments.append(transformParagraphIntoOneSentenceFormat(documentReferent5NoStopWords))
allReferentDocuments.append(transformParagraphIntoOneSentenceFormat(documentReferent6NoStopWords))
allReferentDocuments.append(transformParagraphIntoOneSentenceFormat(documentReferent7NoStopWords))
allReferentDocuments.append(transformParagraphIntoOneSentenceFormat(documentReferent8NoStopWords))
allReferentDocuments.append(transformParagraphIntoOneSentenceFormat(documentReferent9NoStopWords))

#allReferentDocuments.append(transformParagraphIntoOneSentenceFormat(documentReferentUNostopWords))

print 'Now we compute the similarity'

idf_referent= myCalculate_idf(allReferentDocuments[0])

idf_subject = myCalculate_idf(allSubjectDocuments[0])

print len(allSubjectDocuments[0]), idf_subject

def alignment(referent, subject, filename):
    #alignment(studentDocuments, professorsDocuments, filename):
    print 'Alignment 1 '
    print 'We have ', len(referent), 'referent ', len(subject), 'subject'
    i = 0
    f = open(filename,'w')
    while i < len(referent):
        singleReferentDocument = referent[i]
        idf_referent = myCalculate_idf(singleReferentDocument)
        j = 0
        while j < len(singleReferentDocument):
            paraReferent = singleReferentDocument[j]
            k = 0
            while k < len(subject):
                singleSubjectDocument = subject[k]
                #print len(singleDocPro)
                #print '\t ',len(paraStudent)
                sim = selectTheBestSimilarityValue(paraReferent, singleSubjectDocument,idf_referent)
                #print 'StudenDocument id ', i,' studen paragraph ', j ,' prof doc ',k,' paragraphe ',sim[1], 'sim ', sim[0]

                #print  i,' \t', j ,'\t',k,'\t',sim[1], '\t', sim[0],'\t',sim[2]
                f.write(str(i)+' \t'+ str(j) +'\t'+str(k)+'\t'+str(sim[1])+ '\t'+ str(sim[0])+'\t'+sim[2]+'\n')
                k = k + 1
            j = j + 1
        i = i + 1
    f.close()
    return

alignment(allSubjectDocuments, allReferentDocuments, '/Users/velazquezerick/Dropbox/ERICK-PHD/2016/WeekNetherlands/Idea2/Referent1Inverse.txt')