'''
@Author: NI Roger
@Date: 2019-05-29 11:27:58
@LastEditors: NI Roger
@LastEditTime: 2019-06-11 13:07:41
@Description: Test program for WikipediaContent
'''


import WikipediaContent as wkc

if __name__ == "__main__":
    entries = ["aape","mcdonalds","KFC","yoshinoya","adidas","aigle","apple store","asics","asus"]
    wkc.crawlAndWrite(entries,"tempSave.pickle")