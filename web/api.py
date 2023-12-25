import requests
import json 

url = 'http://islomapi.uz/api/present/day?region=Namangan'

data = requests.get(url)

print(data)