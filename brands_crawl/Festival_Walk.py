'''
@Author: NI Roger
@LastEditors: NI Roger
@LastEditTime: 2019-06-11 12:36:30
@Description: Crawler for 'Festival Walk' Website Store Information
'''

from requests_html import HTMLSession
from urllib.parse import urlparse
from urllib.parse import unquote
import requests
from selenium import webdriver
import selenium
import re
session = HTMLSession()


'''
Change the driver_path to fit your environment
See http://chromedriver.chromium.org/ for more info.
'''
driver_path = "./chromedriver.exe"


if __name__ == "__main__":
    print(crawl())


def crawl():
    '''Crawls Store information from 'Festival Walk' website

    Return:
        A dictionary with Store_name as the key and store description as the content
        Note:
            Crawling results may contain non-English characters even though web-pages 
            have been changed to English page.
    '''
    shops_url = []
    for i in [1,2,3]:
        response = session.get("https://www.festivalwalk.com.hk/en/shopping/?cateid="+str(i))
        brand_list = response.html.xpath('//*[@id="masonry"]')

        shops_url += brand_list[0].absolute_links

    shop_desc = {}
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2} # do not load images
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)

    for url in shops_url:
        driver.get(url)
        brand = unquote(urlparse(url).path.split('/')[3])
        shop_desc[brand] = driver.find_element_by_xpath\
            ('//*[@id="contentContainer"]/div[1]/div[4]/div/div[1]/div/div[2]/div/div').text
    
    return shop_desc