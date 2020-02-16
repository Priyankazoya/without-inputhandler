

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import time
import pandas as pd
import Inputhandler




# initializing logging file
logging.basicConfig(format='%(asctime)s: %(levelname)s:%(message)s', filename='myntra.log', level=logging.INFO)

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


info("<myntra>  trying to connecting to url", ' at ',time.ctime())
    
driver = webdriver.Chrome(chrome_options=options)
url='https://www.myntra.com/men-tshirts'
driver.get(url)
# time.sleep(5)
# driver.close()


path="//li[contains(text(),'Page')]"
element=driver.find_element_by_xpath(path)
print(element.text)

looping = int(element.text.split()[-1])




h=[]

p=[]
o=[]
t=[]




header="(//h3[@class='product-brand'])[{}]"
price = "(//span[@class='product-discountedPrice'])[{}]"
offer = "(//span[@class='product-discountPercentage'])[{}]"

for j in range(looping):
    for i in range(1,38):
        
        xpath_header = header.format(i)
        print(i,'-->',Inputhandler.readText(driver,xpath_header),end = " -- ")
        h.append(Inputhandler.readText(driver,xpath_header))
        
        xpath_price = price.format(i)
        print(Inputhandler.readText(driver,xpath_price))
        p.append(Inputhandler.readText(driver,xpath_price))
        
        xpath_offer = offer.format(i)
        print(Inputhandler.getAttribute(driver,xpath_offer,"innerHTML"),end=' -- ')
        o.append(Inputhandler.readText(driver,xpath_offer))
        
        info("fetched date for", ' xpath_header ',time.ctime())
        
    
    page_xpath ="//a[contains(text(),'Next')]"
 
    
    Inputhandler.mouseClick(driver,page_xpath)
    

      
        
        
     
df=pd.DataFrame({'header':h,'price':p,'offer':o,'time':t})
#df.to_csv('amazon.csv')

df.close()
   
    
    
    
    
    
    
    