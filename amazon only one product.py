# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:52:47 2020

@author: Priyanka Zoya
"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import time
# import pandas as pd





# initializing logging file
logging.basicConfig(format='%(asctime)s: %(levelname)s:%(message)s', filename='amazon.log', level=logging.INFO)

# setting options for chrome driver
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument('--disable-infobars')
options.add_argument('--start-fullscreen')
options.add_argument("--disable-popup-blocking")



def info(msg1='',msg2='',msg3=''):
    logging.info(str(msg1)+str(msg2)+str(msg3))
    print(msg1,msg2,msg3)


info("<amazon>  trying to connecting to url", ' at ',time.ctime())
    
driver = webdriver.Chrome(chrome_options=options)
url='https://www.amazon.in/Samsung-Galaxy-Ocean-Blue-64GB/dp/B07HGH3G6H/ref=sr_1_1_sspa?crid=CJJB4043MPKH&keywords=mobile+phones+under+7000&qid=1582525403&sprefix=mob%2Caps%2C619&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFPTlNHSzFGSE9QWDgmZW5jcnlwdGVkSWQ9QTAyOTE3MjhPOFROTFg1SzhGM0ImZW5jcnlwdGVkQWRJZD1BMDgzODg3NDFLWTg2Nzk1SUlMWDQmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
driver.get(url)
# time.sleep(5)
# driver.close()

# h=[]
# r=[]
# p=[]




header = "//span[@id='productTitle']"
rating = "(//span[@id='productTitle']//following::span[@class='a-icon-alt'])[1]"
price = "//span[@id='priceblock_ourprice']"

element=driver.find_element_by_xpath(header)
print(element.text)


element=driver.find_element_by_xpath(rating)
print(element.get_attribute('innerHTML'))


element=driver.find_element_by_xpath(price)
print(element.text)



# df=pd.DataFrame({'header':h,'rating':r,'price':p})
# df