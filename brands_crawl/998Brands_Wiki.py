'''
@Author: NI Roger
@Date: 2019-05-31 15:42:53
@LastEditors: NI Roger
@LastEditTime: 2019-06-11 14:52:03
@Description: Driving program to crawl Wikipedia page for 998 brands
'''

import WikipediaContent as wkc
import json

brands = json.load(open("998brands.json",encoding="UTF-8"))

wkc.crawlAndWrite(brands,"998Wiki.json")