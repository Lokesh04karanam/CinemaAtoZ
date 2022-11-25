from bs4 import BeautifulSoup
import requests 
import urllib.request
import re
import pandas as pd
import json
import csv

url = 'https://www.imdb.com/list/ls000634294/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
response=requests.get(url, headers={"Accept-Language": "en"})
soup=BeautifulSoup(response.text,"html.parser")
movies = soup.select("h3.lister-item-header")

Plot = []
plot = soup.find_all('div',attrs={'class':"lister-item-content"})
for  i in plot:
    x=i.find('p',attrs={'class':""})
    Plot.append(x.text)
list = []
for index in range(0, len(Plot)):
    data = {
        "Plot": Plot[index],
    }
    list.append(data)
    
df = pd.DataFrame(list)
df.to_csv("top250Plot.csv", index=False)

