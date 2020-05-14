import requests


class Github:
    def __init__(self):
        self.apiurl = "https://api.github.com"
        self.token="50791c74e8e9a6560af4b248b727a4df0b995249 "

    def getuser(self, username):
        response = requests.get(self.apiurl+'/users/'+username)
        return response.json()
    def getrepositories(self, username):
        response = requests.get(self.apiurl + '/users/' + username + '/repos')
        return response.json()

    def createrepository(self,name):
        response = requests.post(self.apiurl+'/user/repos?access_token=' +self.token, json={
            "name": name ,
            "description":"ilk repo",
            "homepage" : "https://link.com" ,
            "private":"False",
            "has_issues": True,
            "has_projects":True,
            "has_wiki" : True
        })
        return response.json()
while True:

    secim = input("1. Kullanıcı bul /n 2.repo gör /n 3. repo oluştur /n 4.çık ")

    github = Github()

    if secim == '4':
        break
    else:
        if secim == '1':
            username = input('username: ')
            result = github.getuser(username)
            print(f"name: {result['name']} public repos : {result['public_repos'] } follower :{result['followers']}")
        elif secim == '2':
            username = input('username: ')
            result = github.getrepositories(username)
            for repo in result:
                print(repo['name'])

        elif secim == '3':
            name = input('repo ismi')
            result = github.createrepository(name)
            print(result)