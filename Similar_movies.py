from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import pandas as pd
import json
import csv

url = "https://www.imdb.com/list/ls000634294/?sort=user_rating,desc&st_dt=&mode=detail&page=3"
response = requests.get(url, headers={"Accept-Language": "en"})
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.find_all("h3.lister-item-header")
links = soup.find_all('a',attrs={'href':re.compile("/title/*")})
#Link = [a.attrs.get("href") for a in links]
URL = []
for index in links[1:]:
    URL.append("https://www.imdb.com"+index.attrs.get('href')+"?ref_=ttls_li_tt")
i = 0
for element in URL:
    if i%2 == 0:
        pass
    else:
        URL.remove(element)
    i = i+1
Similar_Movies = []
for i in URL:
    Response = requests.get(i, headers={"Accept-Language": "en"})
    SOUP = BeautifulSoup(Response.content,'html.parser')
    sm = SOUP.find_all('span',attrs={'data-testid':"title"})
    k=0
    l=[]
    for j in sm:
        if(k>2):
            break
        l.append(j.text)
        k=k+1
    Similar_Movies.append(l)

for index in range(0, 100):
    print(Similar_Movies[index])

