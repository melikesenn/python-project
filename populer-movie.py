import requests

class moviedb:

    def __init__(self):
        self.api_url ="https://api.themoviedb.org/3"
        self.api_key ="c3c016ea39d606e2f928cdc30e800f9a"
    def getpopular(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    def search(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()
yeni = moviedb()

while True:
    secim = input("1 populer film \n 2 çıkış \n 3 arama \nseçiniz")

    if secim =="2":
        break
    else:
        if secim == "1":
            movies = yeni.getpopular()
            for movie in movies['results']:
                print(movie['title'])
        elif secim == "3":
            keyword = input("keyword")
            movies = yeni.search(keyword)
            for movie in movies['results']:
                print(movie["name"])

