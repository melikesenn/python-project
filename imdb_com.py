import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'

html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')

list = soup.find('tbody', {"class":"lister-list"}).find_all("tr",limit=10)

for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    year =tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong",{"title":"5.8 based on 9,764 user ratings"}).text
    print(title,year,rating)

