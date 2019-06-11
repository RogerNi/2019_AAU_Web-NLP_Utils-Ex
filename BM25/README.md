# BM25 Search
This package contains a BM25 Search Engine. The engine can return a score indicating the relationship between a given keyword and each passage.

## Algorithms
### Preprocessing of Contents
Contents will be be pre-processed before scoring, which includes following steps:
+ Removing Stop Words (Using NLTK package)
+ Changing words to uniform format to cancel the effects of different formats of words

### Similarities Matrix
A similarities matrix will be constructed to show the relevance among passages. The matrix will be used for scoring later.

### Keyword Scoring
BM25 algorithm is adopted to score the keyword. Besides, the score will be mended by the similarities matrix. The score of one entity will be spreaded to its related entity regarding the relavance in similarities matrix.

## Usage
### Example Program
`BM25_test.py` is a sample program to use `BM25_Search_JSON.py`
### Parameters
Parameter|Description
---|---
`similarity_para`|A variable to control the degree of influence of one entity on another
`spread_times`|A variable to control how many times the spreading will happen 

## Dependencies
### Python Packages
+ json
+ nltk
+ rank_bm25
+ numpy

## Authors
+ **NI Ronghao** - *Initial Work* - [RogerNi](https://github.com/RogerNi)

## Acknowledgments
+ The authors of the packages used here
+ Teachers and friends in Aalborg University who inspire and provide me the chance to write these codes