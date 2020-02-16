# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 23:46:52 2020

@author: Priyanka Zoya
"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# initializing logging file
logging.basicConfig(format='%(asctime)s: %(levelname)s:%(message)s', filename='amazon.log', level=logging.INFO)

# setting options for chrome driver
options = Options()
#options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument('--disable-infobars')
options.add_argument('--start-fullscreen')
options.add_argument("--disable-popup-blocking")



def info(msg1='',msg2='',msg3=''):
    logging.info(str(msg1)+str(msg2)+str(msg3))
    print(msg1,msg2,msg3)
    
    

info("<amazon>  trying to connecting to url", ' at ',time.ctime())

driver = webdriver.Chrome(chrome_options=options)
     
url='https://www.flipkart.com/search?q=freezers&sid=j9e%2Cabm%2Chzg&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_5_na_na_na&as-pos=0&as-type=RECENT&suggestionId=freezers%7CRefrigerators&requestId=c89ead00-8f9a-47e2-a090-f7d8b96f9bb4&as-backfill=on'
driver.get(url)
time.sleep(1)





xpath = "//span[contains(text(),'Page')]"
element=driver.find_element_by_xpath(xpath)
print(element.text)
looping = int(element.text.split()[-1])
 
h=[]
r=[]
p=[]





header ="(//div[@class='_3wU53n'])[{}]" 
rating ="(//div[contains(@class,'hGSR34')])"
price = "(//div[@class='_1vC4OE _2rQ-NK'])[{}]"


for j in range(looping):
    for i in range(1,25):
        
        
        time.sleep(1)
        
        element=driver.find_element_by_xpath(header.format(i))
        print(element.text)
        h.append(element.text)
       
        
        element=driver.find_element_by_xpath(rating.format(i))
        #print(element.get_attribute('innerHTML'))
        print(element.get_attribute('innerHTML').split('<')[0])
        r.append(element.get_attribute)
        
        
        element=driver.find_element_by_xpath(price.format(i))
        print(element.text)
        p.append(element.text)
    
  
    page_xpath ="//span[contains(text(),'Next')]"
    controlClick=driver.find_element_by_xpath(page_xpath)
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, page_xpath)))
    controlClick.click()
 


    
df=pd.DataFrame({'header':h,'rating':r,'price':p})


df



