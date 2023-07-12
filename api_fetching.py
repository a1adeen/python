import requests
import csv 

from requests.api import head


url = "http://api.coincap.io/v2/assets"
response = requests.request("GET" , url , data={})
myjson = response.json()
print(myjson)