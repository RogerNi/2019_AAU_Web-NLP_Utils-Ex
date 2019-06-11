'''
@Author: NI Roger
@Date: 2019-06-11 13:33:05
@LastEditors: NI Roger
@LastEditTime: 2019-06-11 13:38:32
@Description: Crawl 998 brands from website
'''


import requests
from selenium import webdriver
from time import sleep
import selenium
import re

driver_path = ""

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)

def login(username, password):
    driver.find_element_by_id('login-box-email').clear()
    driver.find_element_by_id('login-box-email').send_keys("nironghao@gmail.com")
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys("carmen312")
    driver.find_element_by_xpath('//*[@id="modal-login-container"]/input[2]').click()

def getBrandOnPage():
    b_name_html = driver.find_elements_by_class_name('brand-name')
    return [x.text for x in b_name_html]

def goHome():
    driver.find_element_by_xpath('//*[@id="top1000-table"]/div[3]/button[1]').click()

def nextPage():
    driver.find_element_by_xpath('//*[@id="top1000-table"]/div[3]/button[8]').click()

def scrollDown():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def crawl():
    driver.get("https://www.campaignasia.com/Top1000Brands/Ranking")
    if False:
        login("","")
    brands = []
    try:
        while True:
            sleep(3)
            brands.extend(getBrandOnPage())
            scrollDown()
            nextPage()
    except Exception as e:
        e.with_traceback()
    return brands

if __name__ == "__main__":
    crawl()