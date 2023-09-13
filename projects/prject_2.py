# WEATHER APP
import os
import requests
import json

while True:
    city = input('enter the name of the city')
    url = f'https://api.weatherapi.com/v1/current.json?key=1b24d4111cd64152af3100221231309&q={city}'
    if city == 'quit':
        print('ggs')
        break
    r = requests.get(url)
    # print(r.text)
    dict = json.loads(r.text)
    temp_c = dict['current']['temp_c']
    print(temp_c)
    os.system(f'say {temp_c}')