'''
@Author: NI Roger
@LastEditors: NI Roger
@LastEditTime: 2019-06-11 12:42:30
@Description: Using Google searching result to redirect Wikipedia page
'''


from requests_html import HTMLSession
session = HTMLSession()

def getWikiKeyWordFromGoogle(entry):
    '''Return Wiki Keyword from Google Searching result

    This function first gets the searching result from Google. Then it picks up the wiki links from the
    searching result and choose the most appropriate one.

    Arg:
        entry: Keyword to search
    
    Return:
        One keyword for Wikipedia that is expected to the most suitable one for the input keyword

    Note:
        Frequent HTML requests to Google may cause temporary ban of your IP address from furthur Google 
        search. Also, the strategies to pick up appropriate Wikipedia keyword to choose the minimum-length 
        keyword from all, which is not correct in some situations.
    '''
    responde = session.get("https://www.google.com/search?q="+entry)
    links = responde.html.links
    wikiLinks = [x for x in links if "wikipedia.org" in x]
    wikiKeywords = [x.split("/")[-1] for x in wikiLinks]
    return min(wikiKeywords,key=len)