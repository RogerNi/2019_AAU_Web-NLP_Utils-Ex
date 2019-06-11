'''
@Author: NI Roger
@Date: 2019-06-05 16:03:02
@LastEditors: NI Roger
@LastEditTime: 2019-06-11 13:27:37
@Description: Extract Keywords
'''


#%%
# Extract Keywords from Contents

from rake_nltk import Rake
import json

# load file
wiki = json.load(open("brands_wiki_3.json"))
kw_list = {}

# wiki_values = list(wiki.values())
# wiki_keys = list(wiki.keys())

for i in range(len(wiki)):
    r = Rake(min_length=1, max_length=2)
    r.extract_keywords_from_text(wiki[i]["Wiki_Description"])
    kw_list[wiki[i]["Brand_Name"]] = r.get_ranked_phrases_with_scores()

json.dump(kw_list,open("brands_wiki_3_keywords.json",'w',encoding="UTF-8"))

#%%
# Delete Brands name in Keywords

pass