import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())

list = soup.find_all("li",{"class":"column"},limit=1)

for li in list:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    oldprice = li.find("div",{"class":"proDerail"}).find_all("a")[0].text.strip().strip('TL')
    newprice = li.find("div",{"class":"proDerail"}).find_all("a")[1].text.strip().strip('TL')
    print(name)
    print(link)
    print(oldprice,newprice)

#print(list)