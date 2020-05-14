import requests


def weather(il):
    api_key = "key"
    api_url ="link"
    response = requests.get(f'{api_url}q={il}&cnt=7{api_key}')
    return response.json()





while True:
    islem = input("hava durumunu öğrenmek için 1'e basın \n  çıkmak için 0'a basın ")

    if islem == "0":
        break
    elif islem == "1":
        il = input("hangi ilin havadurumunu öğrenmek istiyorsunuz ?")
        result = weather(il)
        print(result)
    else:
        print("geçersiz işlem")