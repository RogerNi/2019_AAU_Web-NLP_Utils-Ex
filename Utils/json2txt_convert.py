'''
@Author: NI Roger
@Date: 2019-06-06 15:52:28
@LastEditors: NI Roger
@LastEditTime: 2019-06-11 13:28:24
@Description: Temporary Converter between 2 formats
'''


import json
import re
#%%
# start from 477
file_name = "brands_wiki_3_keywords.json"
out_file = "brands_3.txt"
desc = json.load(open(file_name))

index = 477

with open(out_file,'w',encoding='UTF-8') as out:
    for key in desc:
        string = ""+(str(index))+("\t")+(key)
        for i in range(7):
            string += ("\t")
        for kw in desc[key]:
            if kw[1] == key:
                continue
            if re.search('\d+',kw[1]):
                continue
            string += (kw[1])
            string += ('\t')
        out.write(string+"\n")
        index += 1

print("Next index: "+str(index))
    
