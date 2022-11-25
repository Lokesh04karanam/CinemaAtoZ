from home.models import Members
file=open("top100movies.csv","r")
file1=open("top250metascore.csv","r")
file2=open("top100Plot.csv","r")
content=file.readlines()
content1=file1.readlines()
content2=file2.readlines()
for i in range(1,251):
    x=content[i].split(',')
    y=content1[i]
    z=content2[i]
    member=Members(ido=i,Title=x[0],Rating=x[3],IMDb_Rating=x[2],Meta_Rating=y,Cast=x[5:10],Genre=x[10:],Duration=x[4],Plot=z)
    member.save()
#for uploading to members database from the file obtained by scrapping imdb website
    
from home.models import Members
file=open("top100movies.csv","r")
content=file.readlines()
for i in range(506,756):
    x=content[i-505].split(',')
    member=Members.objects.get(id=i)
    member.Year=x[1]
    member.save()
#for uploading year of release to members database from the file obtained by scrapping imdb website
    
from home.models import Members
file=open("top300.csv","r")
content=file.readlines()
for i in range(506,756):
    x=content[i-505]
    member=Members.objects.get(id=i)
    member.Rott_Rating=x
    member.save()
#for uploading rottan tomatoes rating to members database from the file obtained by scrapping imdb website

from home.models import Members
file=open("top300s.txt","r")
content=file.readlines()
for i in range(506,756):
    x=content[i-505]
    member=Members.objects.get(id=i)
    member.similar=x
    member.save()
#for uplaoding similar movies to the members database

from home.models import Members
file=open("review.txt","r")
content=file.readlines()
for i in range(506,756):
    x=content[i-505]
    member=Members.objects.get(id=i)
    member.review=x
    member.save()