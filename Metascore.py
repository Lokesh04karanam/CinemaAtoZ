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

Metascore = [e.text for e in soup.select("span.metascore.favorable")]

list = []

for index in range(0, len(Metascore)):
    data = {
        "Metascore": Metascore[index],
    }
    list.append(data)
    
df = pd.DataFrame(list)
df.to_csv("top250metascore.csv", index=False)

