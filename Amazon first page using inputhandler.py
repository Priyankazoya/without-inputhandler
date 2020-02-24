# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 09:43:02 2019

@author: Priyanka Zoya
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import time
#import sqlite3
# import pandas as pd
import Inputhandler




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
url='https://www.amazon.in/s?k=mobile+phones+under+7000&crid=CJJB4043MPKH&sprefix=mob%2Caps%2C619&ref=nb_sb_ss_i_1_3'
driver.get(url)
# time.sleep(5)
# driver.close()

# h=[]
# r=[]
# p=[]
# t=[]




header="(//h2)[{}]"
rating ="(//h2/following::span[@class='a-icon-alt'])[{}]"
price = '(//span[@class="a-price-whole"])[{}]'

for i in range(1,26):
    xpath_header = header.format(i)
    # h.append(Inputhandler.readText(driver,xpath_header))
    print(i,'-->',Inputhandler.readText(driver,xpath_header),end = " -- ")
    
    xpath_rating = rating.format(i)
    # r.append(Inputhandler.readText(driver,xpath_rating))
    print(Inputhandler.getAttribute(driver,xpath_rating,"innerHTML"),end=' -- ')
    
    xpath_price = price.format(i)
    # p.append(Inputhandler.readText(driver,xpath_price))
    print(Inputhandler.readText(driver,xpath_price))
    info("fetched dat for", ' xpath_header ',time.ctime())
    
     
# df=pd.DataFrame({'header':h,'rating':r,'price':p,'time':t})
#  df.to_csv('amazon.csv')

# df
   
    
    
    
    
    
    
    