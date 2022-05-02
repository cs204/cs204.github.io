import requests
url = "http://termopogoda.ru/data_tomsk.json"
res = requests.get(url).json()['current_temp']
print(res)

