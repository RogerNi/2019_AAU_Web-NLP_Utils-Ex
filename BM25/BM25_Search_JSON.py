'''
@Author: NI Roger
@Date: 2019-05-29 14:39:58
@LastEditors: NI Roger
@LastEditTime: 2019-06-11 15:38:49
@Description: Keyword Ranker adopting BM25 algorithm
'''


import json
from rank_bm25 import BM25Okapi
import numpy as np
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import wordnet 

class BM25_rank:
    '''A keyword searching engine using BM25 to decide the relationship between the keyword and each passage

    Passages are first processed in order to get better performance. First, stopwords are deleted from the 
    contents. Then all the words are changed to Snowball format in order to cancel the effect of different 
    forms of words. Finally, a similarities table will be generated for furthur use.

    Attributes:
        contents: all the contents where we search keyword
        ranker: a BM25 ranker
        similarities: a matrix store the similarities between each pair of passages
        similarities_para: a variable to decide how much similarities will affect the keyword rank
        spread_times: spread how many times
    '''
    contents = {}
    ranker = None
    similarities = []
    similarity_para = 0.0001
    spread_times = 2
    def __init__(self, filePath):
        contentList = json.load(open(filePath,'r',encoding="UTF-8"))
        for c in contentList:
            if not c["Description"]:
                c["Description"] = ''
            self.contents[c["Name"]] = c["Description"]
        # '''
        # Check Non-string
        # '''
        # for key in self.contents:
        #     if type(self.contents[key]) != str:
        #         print(key)
        # '''
        # '''
        self.genRankerAndTable()

    def printKeys(self):
        for content in self.contents:
            print(content)

    def genRankerAndTable(self):
        tokenized = [self.changeToBasicForm(self.filterStopWords(word_tokenize(page))) for page in [self.contents[key] for key in self.contents]]
        self.bm25 = BM25Okapi(tokenized)
        for t in tokenized:
            self.similarities.append(self.bm25.get_scores(t))

    def query(self, keyword):
        tokenized = self.changeToBasicForm(self.getSynonyms(self.filterStopWords(word_tokenize(keyword))))
        raw_score = self.bm25.get_scores(tokenized)
        return self.spreadScore(raw_score, self.spread_times)
        # return self.spreadScore(raw_score, max(len(self.contents) // 10,1))

    def spreadScore(self, raw_score, epochs):
        score = np.asarray(raw_score)
        for e in range(epochs):
            score = np.matmul(score,np.asarray(self.similarities)*self.similarity_para)
        return score

    def filterStopWords(self, words):
        stop_words = set(stopwords.words('english')) 
        filtered = []
        for w in words:
            if w not in stop_words:
                filtered.append(w)
        return filtered

    def changeToBasicForm(self, words):
        snowball_stemmer = SnowballStemmer("english")
        changed = [snowball_stemmer.stem(w) for w in words]
        return changed

    def getSynonyms(self, words):
        synonyms = words.copy()
        for w in words:
            for syn in wordnet.synsets(w):
                for l in syn.lemmas():
                    synonyms.append(l.name())
        print(set(synonyms))
        return synonyms

    def queryRank(self, keyword):
        score = self.query(keyword)
        paired_score = {}
        index = 0
        for c in self.contents:
            paired_score[c] = score[index]
            index += 1
        return sorted(paired_score.items(), key=lambda d: d[1], reverse=True)