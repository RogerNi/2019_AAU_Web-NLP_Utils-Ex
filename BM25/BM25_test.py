'''
@Author: NI Roger
@Date: 2019-05-29 13:14:40
@LastEditors: NI Roger
@LastEditTime: 2019-06-11 12:55:09
@Description: Testing program for BM25_Search_JSON
'''


import BM25_Search_JSON as bms
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

if __name__ == "__main__":
    ranker = bms.BM25_rank("new_town_plaza.json")
    # ranker.printKeys()
    # ranks = ranker.query("electronic")
    ranks = ranker.queryRank("watch")
    print(ranks)
    # print(ranker.similarities)
