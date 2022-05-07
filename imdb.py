import requests
from bs4 import BeautifulSoup
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

html = requests.get(url).content

soup = BeautifulSoup(html,"html.parser")
l = int(input("limiti giriniz..."))
list = soup.find("tbody",{"class":"lister-list"}).find_all('tr',limit=l)
a = 0
for i in list:
    x = i.find("td",{"class":"titleColumn"}).find("a").text
    y = i.find("td",{"class":"ratingColumn imdbRating"}).strong.string
    year = i.find("td",{"class":"titleColumn"}).span.text.strip("()")
    a += 1
    print(f"{str(a).center(3)} -- {x.center(55)}Rating:{y} ---- year {year}")
