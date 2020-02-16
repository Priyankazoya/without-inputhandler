

import requests
import bs4
import pandas as pd

url = 'https://www.timeanddate.com/weather/india'
res=requests.get(url)
soup=bs4.BeautifulSoup(res.text,'lxml')

city = []
temp=[]
weather=[]
date_time=[]

for i in soup.find_all("td"):
    print(i)

for i in range(0,len(soup.find_all("td")),4):
    print(i)

    data = soup.find_all("td")[i]
    print(str(data).split('>')[2].split('<')[0])
    city.append(str(data).split('>')[2].split('<')[0])
    
    data = soup.find_all("td")[i+1]
    print(str(data).split('>')[1].split('<')[0])
    date_time.append(str(data).split('>')[1].split('<')[0])
    
    data = str(soup.find_all("td")[i+2])
    print(data[data.find('title=')+6:data.find('width=')])
    weather.append(data[data.find('title=')+6:data.find('width=')])
    
    
    data=str(soup.find_all("td")[i+3])
    print(data.split('>')[1].split('<')[0])
    temp.append(data.split('>')[1].split('<')[0])
    
    
    
df=pd.DataFrame({'city':city,'temparature':temp,'weather':weather,'date_time':date_time})
df.to_csv('weatherreport.csv')