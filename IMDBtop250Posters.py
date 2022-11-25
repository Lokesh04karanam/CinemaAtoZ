from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import pandas as pd
import json
import csv

url = "http://www.imdb.com/chart/top"
response = requests.get(url, headers={"Accept-Language": "en"})
soup = BeautifulSoup(response.text, "html.parser")

Images=[]
img_links=soup.select('img[src^="https://m.media-amazon.com/images/M"]')

for i in range(len(img_links)):
	Images.append(img_links[i]['src'])
	
#print(Images)
for i in range(len(Images)):
       #Copies a network object denoted by a url to a local file
	name="/home/loki/img/"+str(i+1)+".jpg"
	urllib.request.urlretrieve(Images[i], name)


