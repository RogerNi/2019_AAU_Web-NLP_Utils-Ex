'''
@Author: NI Roger
@Date: 2019-05-29 11:46:13
@LastEditors: NI Roger
@LastEditTime: 2019-06-11 12:55:37
@Description: Testing program for GoogleRedirect
'''


import GoogleRedirect as gred

if __name__ == "__main__":
    words = gred.getWikiKeyWordFromGoogle("starbucks")
    print(words)