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
Certificate = [a.text for a in soup.select("span.certificate")]
Runtime = [b.text for b in soup.select("span.runtime")]
Genre = [c.text for c in soup.select("span.genre")]
IMDb = []
imdb = soup.find_all('div',attrs={'class':"ipl-rating-star small"})
for  i in imdb:
    x=i.find('span',attrs={'class':"ipl-rating-star__rating"})
    IMDb.append(x.text)
Metascore = [e.text for e in soup.select("span.metascore.favorable")]
Plot = [f.text for f in soup.find('p',attrs={'class':""})]
Cast=[]
cast = soup.find_all('p',attrs={'class':"text-muted text-small"})
for i in cast:
    x = i.find_all('a',attrs={'href':re.compile("/name/nm*")})
    l = []
    if x != []:
      for j in x:
          l.append(j.text)
    else: continue
    Cast.append(l)


list = []

for index in range(0, len(movies)):
    movie_string = movies[index].get_text()
    movie = " ".join(movie_string.split()).replace(".", "")
    movie_title = movie[len(str(index)) + 1 : -7]
    year = re.search("\((.*?)\)", movie_string).group(1)
    place = movie[: len(str(index)) - (len(movie))]

    data = {
        "place": place,
        "movie_title": movie_title,
        "year": year,
        "IMDb": IMDb[index],
        "Certificate": Certificate[index],
        "Runtime": Runtime[index],
        "Genre": Genre[index],
        "star_cast": Cast[index],
    }
    list.append(data)
    
    
for movie in list:
    print(
        movie["place"],
        "-",
        movie["movie_title"],
        "(" + movie["year"] + ") -",
        "Starring:",
        movie["star_cast"],
        movie["IMDb"],
        movie["Certificate"],
        movie["Runtime"],
        movie["Genre"],
    )
    
    
df = pd.DataFrame(list)
df.to_csv("top250movies.csv", index=False)

    
    
    
    
    
