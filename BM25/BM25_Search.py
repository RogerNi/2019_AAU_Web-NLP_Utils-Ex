'''
@Author: NI Roger
@Date: 2019-05-29 13:05:52
@LastEditors: NI Roger
@LastEditTime: 2019-06-11 12:54:43
@Description: Older Version of BM25_Search_JSON
'''


import pickle
from rank_bm25 import BM25Okapi
import numpy as np
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer

class BM25_rank:
    '''Old Version of BM25_Search_JSON

    See BM25_Search_JSON documents
    '''
    contents = {}
    ranker = None
    similarities = []
    similarity_para = 0.1
    def __init__(self, filePath):
        self.contents = pickle.load(open(filePath,'rb'))
        self.genRankerAndTable()

    def printKeys(self):
        for content in self.contents:
            print(content)

    def genRankerAndTable(self):
        tokenized = [self.changeToBasicForm(self.filterStopWords(word_tokenize(page[0]))) for page in [self.contents[key] for key in self.contents]]
        self.bm25 = BM25Okapi(tokenized)
        for t in tokenized:
            self.similarities.append(self.bm25.get_scores(t))

    def query(self, keyword):
        tokenized = self.changeToBasicForm(self.filterStopWords(word_tokenize(keyword)))
        raw_score = self.bm25.get_scores(tokenized)
        return self.spreadScore(raw_score, max(len(self.contents) / 10,1))

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