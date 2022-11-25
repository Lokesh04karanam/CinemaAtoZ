from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
#this is used for scraping the user reviews of the movie
url = 'https://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
photos = soup.find_all('td',attrs={'class': "posterColumn"})
movlin = []
k = 0
#here we have used the sessions because we need to enter into to user review page 
#here we have taken advantage of movie connections in the alltopics button on the nav bar at the top of the page
for i in photos:
    if(k>50):
        break
    movlin.append("https://www.imdb.com"+i.a['href']+"reviews?ref_=tt_ql_sm")
    k = k+1
with requests.session() as s:
    w = s.get(url)
    for i in movlin:
        x = s.get(i)
        t = BeautifulSoup(x.content,'html5lib')
        y = t.find_all('a',attrs={'href':re.compile("/review/rw*"),'class':"title"})
        l = 0
        r = []
        for i in y:
            if l>6:
                break
            r.append(re.sub('\n',"",i.text))
            l = l+1#we are using only 6 of the reviews because of the space in template
        print(r)
            