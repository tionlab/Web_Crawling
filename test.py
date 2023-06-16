from selenium import webdriver
import urllib
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os
import sys
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
if getattr(sys, "frozen", False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path, options=options)
else:
    driver = webdriver.Chrome(options=options)

inputtext = input('검색어 : ')

def imageDown(keyword):
    url = f'https://www.google.com.br/search?q={keyword}&source=lnms&tbm=isch'
    driver.get(url)
    driver.implicitly_wait(5)
    # body = driver.find_element_by_css_selector('body')
    body = driver.find_element(By.CSS_SELECTOR, 'body')
    for i in range(30):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
    #imgs = driver.find_elements_by_css_selector('img.rg_i')
    imgs = driver.find_elements(By.CSS_SELECTOR, 'img.rg_i')
    os.makedirs(keyword, exist_ok=True)
    time.sleep(10)
    for idx, img in enumerate(imgs):
        print(idx,img.get_attribute('src'))
        imgUrl = img.get_attribute('src')
        if imgUrl == None:
            break
        imgName = f'./{keyword}/{keyword+str(idx)}.jpg'
        urllib.request.urlretrieve(imgUrl, imgName)

imageDown(inputtext)
